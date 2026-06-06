class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0

        for price in prices:
            lowest = min(lowest, price)

            profit = price - lowest

            best = max(best, profit)

        return best