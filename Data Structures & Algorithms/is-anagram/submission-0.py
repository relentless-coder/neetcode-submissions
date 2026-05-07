class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dt = {}

        for c in s:
            if c in dt:
                dt[c] += 1
            else:
                dt[c] = 1
        
        for b in t:
            if b not in dt:
                return False
            dt[b] -= 1
        
        for d in dt:
            if dt[d] != 0:
                return False
        
        return True