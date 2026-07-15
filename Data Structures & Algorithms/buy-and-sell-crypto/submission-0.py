class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
       
 
            l
        10  1  5  6  7 1
                       r
        create pointer l
        create max_profit = 0

        create a for loop to move r from 1 :
        find profit
        if profit >0:
            continue
            update profit
        else:
            l = r
        return max_profit

        """
        max_profit = 0
        l =0
        for r in range(1, len(prices)):
            profit = prices[r]-prices[l]
            if profit >0:
                max_profit = max(max_profit, profit)
                continue
            else:
                l =r
        return max_profit
        