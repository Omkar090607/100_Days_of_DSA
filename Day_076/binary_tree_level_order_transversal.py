class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            n = len(queue)

            for i in range(n):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
