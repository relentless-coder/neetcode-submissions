class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        last_el = nums[len(nums) - 1]
        min_idx = -1
        while lo <= hi:
            m = (lo + hi) // 2
            if nums[m] > last_el:
                lo = m + 1
            else:
                min_idx = m
                hi = m - 1
        print(min_idx)
        if nums[min_idx] == target:
            return min_idx
        lo, hi = 0, min_idx - 1
        if target <= last_el:
            lo, hi = min_idx, len(nums) - 1
        print(lo, hi)
        while lo <= hi:
            m = (lo + hi) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                hi = m - 1
            else:
                lo = m + 1
        return -1