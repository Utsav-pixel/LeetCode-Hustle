from typing import List
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        Profit = 0
        BuyAmt = prices[0]
        for i in range(1,len(prices)):
            if prices[i] <BuyAmt :
                BuyAmt = min(prices[i],BuyAmt)
            else:
                Profit =max(Profit, prices[i] - BuyAmt )
        return Profit
    

a = [7,1,5,3,6,4]

Sol = Solution()
print(Sol.maxProfit(a))