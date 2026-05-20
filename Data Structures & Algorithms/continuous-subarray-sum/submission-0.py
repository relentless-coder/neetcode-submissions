class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dt = {0: -1}
        n = len(nums)
        pref = [0]*n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i]

        for i in range(n):
            r = pref[i]%k
            if r in dt:
                if i - dt[r] >= 2:
                    return True
            else:
                dt[r] = i
        
        return False