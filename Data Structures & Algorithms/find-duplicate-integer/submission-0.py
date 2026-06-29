class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            val = abs(nums[i])
            val_at_index = nums[val]

            if val_at_index < 0:
                return val
            
            nums[val] *= -1
"""
[1,-2,-3,-2,2]
 0 1 2 3 4

"""