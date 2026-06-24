class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        i = 0
        j = m

        while i <= j:
            mid = (j-i)//2 + i

            left1 = float("-inf") if mid == 0 else nums1[mid-1]
            right1 = float("inf") if mid == m else nums1[mid]

            len1 = mid
            len2 = (m+n+1)//2 - len1

            left2 = nums2[len2-1] if 0 <= len2-1 < n else float("-inf")
            right2 = nums2[len2] if 0 <= len2 < n else float("inf")

            if max(left1, left2) <= min(right1, right2):
                if (m+n)%2 == 0:
                    return (max(left1, left2)+min(right1, right2))/2
                else:
                    return max(left1, left2)
            elif max(left1, left2) > min(right1, right2):
                i = mid + 1
            else:
                j = mid -1
        return 0
"""
nums1 = [1,2]
         i mj
nums2 = [3]

left1 = 1
right1 = 2

left2 = 3
right2 = inf
"""