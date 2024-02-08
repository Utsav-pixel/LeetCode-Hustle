from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        outList = []
        for i,value in enumerate(nums):
            try:
                seen_dict[target-value]
                return [seen_dict[target-value],i]
            except:
                seen_dict[value]=i