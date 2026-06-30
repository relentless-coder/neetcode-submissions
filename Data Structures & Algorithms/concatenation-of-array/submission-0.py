class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*(2*n)
        p = 0
        for i in range(2*n):
            if i % n == 0:
                p = 0
            ans[i] = nums[p]
            p += 1
        return ans

        