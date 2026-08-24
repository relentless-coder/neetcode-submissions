import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def compare_freq_map(t, curr):
            for c in t:
                if curr.get(c, 0) < t[c]:
                    return False
            return True


        l = 0
        best_len = len(s) + 1
        best_idx = -1
        t_freq = {}
        s_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
        required = len(t_freq.keys())
        satisfied = 0
        
        for r in range(len(s)):
            s_freq[s[r]] = s_freq.get(s[r], 0) + 1
            if s_freq[s[r]] == t_freq.get(s[r], 0):
                satisfied += 1
            while satisfied == required:
                prev = best_len
                best_len = min(best_len, r - l + 1)
                if prev != best_len:
                    best_idx = l
                if s_freq.get(s[l], 0) > t_freq.get(s[l], 0):
                    if s_freq.get(s[l], 0) == t_freq.get(s[l], 0):
                        satisfied -= 1
                    s_freq[s[l]] -= 1
                    l += 1
                else:
                    break
        if best_idx == -1:
            return ""
        return s[best_idx:best_idx + best_len]

        