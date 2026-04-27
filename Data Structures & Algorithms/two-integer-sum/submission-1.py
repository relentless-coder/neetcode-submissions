class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairDict = {}
        for i,num in enumerate(nums):
            pairDict[target - num] = i
        print(pairDict)
        for i,num in enumerate(nums):
            if num in pairDict and i != pairDict[num]:
                return [i, pairDict[num]]