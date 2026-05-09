class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dt = {}
        ln = len(nums)
        for n in nums:
            if n in dt:
                dt[n] += 1
            else:
                dt[n] = 1
        
        for k in dt:
            if dt[k] > ln/2:
                return k
