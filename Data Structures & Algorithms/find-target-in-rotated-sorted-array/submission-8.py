class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            while left <= right:
                m = (left + right) // 2
                if nums[m] == target:
                    return m
                if target > nums[m]:
                    left = m + 1
                else:
                    right = m - 1
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        left_search = binary_search(0, l - 1)
        if left_search != -1:
            return left_search
        return binary_search(l, len(nums) - 1)
        

