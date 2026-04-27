class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        last_el = nums[len(nums) - 1]
        min_index = -1
        while lo <= hi:
            m = (lo + hi) // 2
            if nums[m] > last_el:
                lo = m + 1
            else:
                min_index = m
                hi = m - 1
        return nums[min_index]