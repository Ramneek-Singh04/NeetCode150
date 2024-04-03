class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxprofit = 0
        buy = 100000
        sell = 0
        for i in prices:
            if i < buy:
                buy = i
            elif i > buy:
                sell = i
                profit = sell - buy
            if profit > maxprofit:
                maxprofit = profit
        return maxprofit

