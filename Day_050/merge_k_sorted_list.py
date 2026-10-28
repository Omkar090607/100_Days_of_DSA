# LeetCode - Merge K Sorted Lists
# Difficulty: Hard
# Topics: Linked List, Divide and Conquer, Heap (Priority Queue)
# Runtime: 7ms, Beats 84.88%
# Memory: 22.98MB, Beats 50.61%

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            value, i, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

