class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0]*n
        suf = [0]*n

        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] + nums[i + 1]
        for i in range(len(nums)):
            if pref[i] == suf[i]:
                return i
        
        return -1