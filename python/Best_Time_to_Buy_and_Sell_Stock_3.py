from typing import List
import heapq
class Solution:
    def maxProfit(self, price: List[int]) -> int:
        n = len(price)

        # profitBar = []
        # Index = []
        # for i in range(1,len(prices)):
        #     if prices[i]>prices[i-1]:
        #         if len(Index)==0 or Index[-1][1]!=i-1:
        #             Index.append([i-1,i])
        #             profitBar.append(prices[i]-prices[i-1])
        #         elif  Index[-1][1]==i-1:
        #             Index[-1][1] = i
        #             profitBar[-1] +=prices[i]-prices[i-1]
        # print(Index)
        # print(profitBar)
        # if len(profitBar)>2:
        #     return sum(heapq.nlargest(2, profitBar))
        # else:
        #     return sum(profitBar)
a = [1,2,4,2,5,7,2,4,9,0]
Sol = Solution()
print(Sol.maxProfit(a))
