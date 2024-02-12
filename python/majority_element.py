
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Counter = {}
        for i in nums:
            try:
                Counter[i]+=1
                if Counter[i]>len(nums)//2:
                    return i
            except:
                Counter[i]=1

        return nums[0]
            
a = [2,2,1,1,1,2,2]


Sol = Solution()
print(Sol.majorityElement(a))