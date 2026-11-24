class Solution:
    def buildTree(self, preorder, inorder):
        # Store the index of each value in inorder
        positions = {value: i for i, value in enumerate(inorder)}
        index = 0

        def build(left, right):
            nonlocal index

            if left > right:
                return None

            # The next preorder value is the root
            value = preorder[index]
            index += 1

            root = TreeNode(value)

            # Build the left and right subtrees
            mid = positions[value]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)