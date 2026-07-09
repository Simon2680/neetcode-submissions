class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final = 0
        maxSells = [0] * len(prices)
        for i in reversed(range(len(prices) - 1)):
            maxSells[i] = max(prices[i+1],maxSells[i+1])
            final = max(final, maxSells[i] - prices[i])
        
        return final

        