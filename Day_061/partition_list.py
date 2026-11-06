class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0)
        greater = ListNode(0)

        less_tail = less
        greater_tail = greater

        while head:
            if head.val < x:
                less_tail.next = head
                less_tail = less_tail.next
            else:
                greater_tail.next = head
                greater_tail = greater_tail.next

            head = head.next

        greater_tail.next = None
        less_tail.next = greater.next

        return less.next