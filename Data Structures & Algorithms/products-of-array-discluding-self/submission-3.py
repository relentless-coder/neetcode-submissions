class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProd = [1]*n
        suffixProd = [1]*n
        res = [1]*n

        for i in range(1, n):
            prefixProd[i] = prefixProd[i - 1]*nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffixProd[i] = suffixProd[i + 1]*nums[i + 1]

        for i in range(n):
            res[i] = prefixProd[i]*suffixProd[i]
        
        return res

