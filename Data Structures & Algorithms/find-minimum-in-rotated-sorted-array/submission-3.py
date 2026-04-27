class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        last_el = nums[len(nums) - 1]
        min_index = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > last_el:
                l = m + 1
            else:
                min_index = m
                r = m - 1
        return nums[min_index]
