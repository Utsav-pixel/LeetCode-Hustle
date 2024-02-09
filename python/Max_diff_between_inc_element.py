from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i = nums[0]
        max_diff = 0
        for j in range(1,len(nums)):
            i = min(nums[j],i)
            max_diff = max(max_diff,nums[j]-i)
        if max_diff<=0:
            return -1
        return max_diff