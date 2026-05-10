class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dt = {}
        arr = [[] for _ in range(n + 1)]
        res = []
        for a in nums:
            if a in dt:
                dt[a] += 1
            else:
                dt[a] = 1
        print(dt)
        for t in dt:
            fr = dt[t]
            arr[fr].append(t)
        
        
        for i in range(len(arr) - 1, -1, -1):
            if len(res) == k:
                break
            if len(arr[i]) > 0:
                res.extend(arr[i])
        
        return res
        
