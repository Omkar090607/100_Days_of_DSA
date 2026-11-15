
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(start, end):
            if start > end:
                return [None]

            trees = []

            for i in range(start, end + 1):
                left_trees = build(start, i - 1)
                right_trees = build(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return build(1, n)