from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = SortedList()

        i = 0
        ans = []

        while i <= len(nums):
            if len(pq) < k and i < len(nums):
                pq.add(nums[i])
                i += 1
                continue
            if len(pq) < k:
                break
            # print(pq, nums[i-k])
            max_val = pq[-1]
            ans.append(max_val)
            pq.remove(nums[i-k])
        
        return ans