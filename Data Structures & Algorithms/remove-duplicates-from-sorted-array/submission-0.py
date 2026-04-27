class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lo = 0
        hi = 1
        initial_len = len(nums)
        removed = 0
        while hi < len(nums):
            if nums[lo] == nums[hi]:
                nums.pop(lo)
                removed += 1
            else:
                lo += 1
                hi += 1
        
        return initial_len - removed
