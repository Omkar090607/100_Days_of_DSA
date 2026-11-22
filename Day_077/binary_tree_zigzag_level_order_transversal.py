class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        queue = [root]
        left_to_right = True

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

            if not left_to_right:
                level.reverse()

            result.append(level)
            left_to_right = not left_to_right

        return result
