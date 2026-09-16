"""Update the dates of the last 11 commits in the current Git repository."""

import os
import subprocess
import sys


TARGET_DATES = [
    f"2026-09-{day:02d}T12:00:00"
    for day in range(7, 18)
]


def git(*args, env=None):
    """Run Git without invoking a shell, so this works in CMD and PowerShell."""
    return subprocess.check_output(
        ["git", *args],
        env=env,
        stderr=subprocess.STDOUT,
        text=True,
    ).strip()


def main():
    try:
        git("rev-parse", "--git-dir")
        commits = git("rev-list", "HEAD").splitlines()
    except subprocess.CalledProcessError as error:
        print(f"Git error: {error.output.strip()}", file=sys.stderr)
        return 1

    if len(commits) < len(TARGET_DATES):
        print(
            f"Error: HEAD has {len(commits)} commits; "
            f"{len(TARGET_DATES)} are required.",
            file=sys.stderr,
        )
        return 1

    commits_to_change = list(reversed(commits[:len(TARGET_DATES)]))
    parent = commits[len(TARGET_DATES)] if len(commits) > len(TARGET_DATES) else None

    print(f"Rebuilding the last {len(TARGET_DATES)} commits from oldest to newest...")

    for day, (commit, target_date) in enumerate(
        zip(commits_to_change, TARGET_DATES), start=1
    ):
        tree = git("show", "-s", "--format=%T", commit)
        message = git("show", "-s", "--format=%B", commit)

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = target_date
        env["GIT_COMMITTER_DATE"] = target_date

        command = ["commit-tree", tree]
        if parent:
            command.extend(["-p", parent])
        command.extend(["-F", "-"])

        new_commit = subprocess.run(
            ["git", *command],
            input=message,
            text=True,
            capture_output=True,
            check=True,
            env=env,
        ).stdout.strip()

        print(f"Day {day:02d} ({target_date}): {commit[:7]} -> {new_commit[:7]}")
        parent = new_commit

    subprocess.run(["git", "reset", "--hard", parent], check=True)
    print("Success: local branch now points to the rebuilt commit history.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())