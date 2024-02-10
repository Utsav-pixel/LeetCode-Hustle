from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for i,value in enumerate(nums):
            req_index = seen_dict.get(target-value)
            if req_index is not None:
                return [req_index,i]
            else:
                seen_dict[value]=i
        return []

Sol = Solution()
print(Sol.twoSum([2,7,11,5],9))