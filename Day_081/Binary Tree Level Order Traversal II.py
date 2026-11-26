from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result[::-1]