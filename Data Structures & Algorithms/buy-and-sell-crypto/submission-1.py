class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            current_profit = prices[i] - minPrice
            if current_profit > profit:
                profit = current_profit
            minPrice = min(minPrice, prices[i])
        return profit        
        