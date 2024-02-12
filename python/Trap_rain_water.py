from typing import List
class Solution:
    def trap(self,height: List[int]) -> int:
        lmax = [0]*len(height)
        rmax = [0]*len(height)
        lmax[0] = height[0]
        rmax[-1]= height[-1]
        for i in range(1,len(lmax)):
            lmax[i] = max(lmax[i-1], height[i])
            rmax[len(rmax)-i-1] = max(rmax[len(rmax)-i], height[len(rmax)-1-i])
        res = 0
        for i in range(1, len(height)-1):
            res += min(lmax[i],rmax[i])-height[i]
        return res
a = [7, 1, 5, 3, 6, 4]
Sol = Solution()
print(Sol.trap(a))
