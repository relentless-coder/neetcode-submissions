class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i, j = 0, 1
        nums.sort()
        while j < len(nums):
            if nums[i] == nums[j]:
                return True
            else:
                i = i + 1
                j = j + 1
        return False
         