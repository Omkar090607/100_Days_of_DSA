# LeetCode - Remove Nth Node From End of List
# Difficulty: Medium
# Topics: Linked List, Two Pointers
# Runtime: 0ms, Beats 100.00%
# Memory: 19.26MB, Beats 62.54%

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next