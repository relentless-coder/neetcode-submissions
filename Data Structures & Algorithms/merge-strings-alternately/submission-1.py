class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        s = ''
        while l < len(word1) and r < len(word2):
            s += word1[l]
            s += word2[r]
            l += 1
            r += 1
        
        if l < len(word1):
            for x in range(l, len(word1)):
                s += word1[x]
        else:
            for x in range(r, len(word2)):
                s += word2[x]
        
        return s
        