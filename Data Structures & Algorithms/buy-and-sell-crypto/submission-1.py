class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        suff = [0] * n

        suff[n-1] = -1

        for i in range(n-2, -1, -1):
            suff[i] = max(suff[i+1], prices[i+1])
        
        # suff = [7,7,7,7,1,-1]
        # print(suff)

        max_profit = 0

        for i in range(n-1):
            max_sell_price = suff[i]
            profit = max_sell_price - prices[i]

            max_profit = max(max_profit, profit)
        
        return max_profit