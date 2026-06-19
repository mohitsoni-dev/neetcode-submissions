class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n-1

        ans = 10001

        while i <= j:
            mid = (j-i)//2 + i

            # if left sorted
            is_left_sorted = (nums[i] <= nums[mid])
            if is_left_sorted:
                ans = min(ans, nums[i])
                i = mid + 1
            else:
                ans = min(ans, nums[mid])
                j = mid - 1

        return ans

"""
[3,4,5,6,1,2]
 i   m     j
"""