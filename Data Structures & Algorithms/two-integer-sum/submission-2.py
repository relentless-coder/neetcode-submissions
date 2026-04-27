class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairDict = {}
        for i,num in enumerate(nums):
            k = target - num
            if k in pairDict:
                return [pairDict[k], i]
            else:
                pairDict[num] = i