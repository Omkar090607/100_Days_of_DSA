class Solution:
    def buildTree(self, inorder, postorder):
        # Store the positions of values in inorder
        positions = {value: i for i, value in enumerate(inorder)}
        index = len(postorder) - 1

        def build(left, right):
            nonlocal index

            if left > right:
                return None

            # The last postorder value is the root
            value = postorder[index]
            index -= 1

            root = TreeNode(value)
            mid = positions[value]

            # Build the right subtree first, then the left
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)