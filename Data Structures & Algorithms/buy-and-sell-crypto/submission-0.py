class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for buy_day in range(len(prices)):
            for sell_day in range(buy_day+1, len(prices)):
                if prices[sell_day] - prices[buy_day] > profit:
                    profit = prices[sell_day] - prices[buy_day]
                else:
                    continue
        return profit

        