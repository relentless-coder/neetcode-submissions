class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dt = {}
        for num in nums:
            if num in dt:
                return True
            dt[num] = True
        return False
        