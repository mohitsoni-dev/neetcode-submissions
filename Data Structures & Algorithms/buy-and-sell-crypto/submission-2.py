class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        n = len(prices)
        max_profit = 0


        while i <= j and j < n:
            if i == j:
                j += 1
            elif prices[i] > prices[j]:
                i = j
            else:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
                j += 1
        
        return max_profit