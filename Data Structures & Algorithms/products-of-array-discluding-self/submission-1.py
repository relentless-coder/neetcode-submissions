class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        for i in range(len(nums)):
            prod = 1
            if i - 1 < 0:
                for j in range(i + 1, len(nums)):
                    prod *= nums[j]
            elif i + 1 > len(nums):
                for j in range(0, i):
                    prod *= nums[j]
            else:
                for j in range(0, i):
                    prod *= nums[j]
                for j in range(i + 1, len(nums)):
                    prod *= nums[j]
            res.append(prod)
        return res
