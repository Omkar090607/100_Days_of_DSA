# LeetCode 4 - Median of Two Sorted Arrays
#
# Difficulty: Hard
#
# Topic: Array, Binary Search, Divide and Conquer
#
# Runtime: 1ms (Beats 58.02%)
#
# Memory: 19.59MB (Beats 43.11%)

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            # Boundary values around the partitions
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")

            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            # Correct partition found
            if left1 <= right2 and left2 <= right1:

                # Odd total length
                if total % 2 == 1:
                    return max(left1, left2)

                # Even total length
                return (max(left1, left2) + min(right1, right2)) / 2.0

            # Partition in nums1 is too far right
            elif left1 > right2:
                right = i - 1

            # Partition in nums1 is too far left
            else:
                left = i + 1