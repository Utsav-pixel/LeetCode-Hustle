from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSum = nums[0]
        LastSum = nums[0]
        for i in range(1,len(nums)):
            LastSum = max(LastSum+nums[i],nums[i])
            MaxSum = max(MaxSum,max(LastSum+nums[i],nums[i]))

        return MaxSum

        

a = [-7,1,5,3,6,4]

Sol = Solution()
print(Sol.maxSubArray(a))