class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProd = [1]*n
        suffixProd = [1]*n
        res = []

        for i in range(n):
            if i > 0:
                prefixProd[i] = prefixProd[i - 1]*nums[i]
            else:
                prefixProd[0] = nums[0]
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                suffixProd[i] = suffixProd[i + 1]*nums[i]
            else:
                suffixProd[i] = nums[i]

        for i in range(n):
            if i == 0:
                res.append(suffixProd[1])
            elif i == len(nums) - 1:
                res.append(prefixProd[i - 1])
            else:
                res.append(prefixProd[i - 1]*suffixProd[i + 1])
        
        return res

