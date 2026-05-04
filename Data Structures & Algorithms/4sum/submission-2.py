class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 1):
            if nums[i] > target:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                l,r = j+1, len(nums) - 1
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                sm = target - (nums[i] + nums[j])
                while l < r:
                    if nums[l] + nums[r] > sm:
                        r -= 1
                    elif nums[l] + nums[r] < sm:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
            
        
        return res