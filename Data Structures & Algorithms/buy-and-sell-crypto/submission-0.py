class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        buy = prices[0]

        for num in prices:
            profit = num - buy
            if profit > best:
                best = profit
            if num < buy:
                buy = num
        
        return best