from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        inc =0
        dre =0

        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                inc+=1
            elif nums[i]>nums[i+1]:
                dre+=1
        if dre ==0:
            return True
        elif inc-dre == inc-1:
            if nums[-1]<nums[0]:
                inc+=1
            elif nums[0]<nums[-1]:
                dre+=1
            if inc-dre == inc-1:
                return True
        return False
