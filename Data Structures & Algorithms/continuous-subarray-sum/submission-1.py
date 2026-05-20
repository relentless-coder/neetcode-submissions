class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dt = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            r = total%k
            if r in dt:
                if i - dt[r] >= 2:
                    return True
            else:
                dt[r] = i
        
        return False