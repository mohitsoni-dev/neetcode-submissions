class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)

        ans = j

        while i <= j:
            k = (j-i)//2 + i

            can_finish = self.can_finish(piles, k, h)
            if can_finish:
                ans = k
                j = k - 1
            else:
                i = k + 1
        
        return ans

    def can_finish(self, piles: list[int], k: int, h: int):
        total_time = 0

        for pile in piles:
            time = (pile//k) + (1 if pile%k != 0 else 0)
            total_time += time
  
        return total_time <= h