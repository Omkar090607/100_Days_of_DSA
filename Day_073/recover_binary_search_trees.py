
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = None
        second = None
        prev = None
        curr = root

        while curr:
            if curr.left is None:
                # Check whether the current node is misplaced
                if prev and prev.val > curr.val:
                    if first is None:
                        first = prev
                    second = curr

                prev = curr
                curr = curr.right

            else:
                # Find the inorder predecessor
                predecessor = curr.left

                while predecessor.right and predecessor.right is not curr:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    # Create a temporary link
                    predecessor.right = curr
                    curr = curr.left
                else:
                    # Remove the temporary link
                    predecessor.right = None

                    if prev and prev.val > curr.val:
                        if first is None:
                            first = prev
                        second = curr

                    prev = curr
                    curr = curr.right

        # Swap the misplaced values
        if first and second:
            first.val, second.val = second.val, first.val
