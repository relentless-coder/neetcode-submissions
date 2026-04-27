class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        check_count = [0] * 26
        window = [0] * 26
        a = ord("a")
        for i in range(len(s1)):
            check_count[ord(s1[i]) - a] += 1
            window[ord(s2[i]) - a] += 1
        if check_count == window:
            return True
        l = 0
        k = len(s1)
        for r in range(k, len(s2)):
            l = r - k
            window[ord(s2[l]) - a] -= 1
            window[ord(s2[r]) - a] += 1
            if window == check_count:
                return True
        return False
        