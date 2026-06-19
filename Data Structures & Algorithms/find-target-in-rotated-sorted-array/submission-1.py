class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n-1

        while i <= j:
            mid = (j-i)//2 + i

            if nums[mid] == target:
                return mid
            
            is_left_sorted = nums[i] <= nums[mid]

            # if is_left_sorted and nums[i] <= target <= nums[mid]:
            #     j = mid - 1
            # elif not is_left_sorted and nums[mid] <= target <= nums[j]:
            #     i = mid + 1

            if is_left_sorted:
                if nums[i] <= target <= nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] <= target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        
        return -1
            

"""
[5,1,3]
 i m j
"""