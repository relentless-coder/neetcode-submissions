class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        best_len = float("inf")
        sm = 0
        for r in range(len(nums)):
            sm += nums[r]
            while sm >= target:
                best_len = min(best_len, r - l + 1)
                sm -= nums[l]
                l += 1
        if best_len == float("inf"):
            return 0
        return best_len
        