class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_count = {}
        max_freq = 0
        length = 0
        l = 0
        for r in range(len(s)):
            freq_count[s[r]] = freq_count.get(s[r], 0) + 1
            if (r - l + 1) - max(freq_count.values()) > k:
                freq_count[s[l]] = freq_count.get(s[l]) - 1
                l += 1
            length = max(length, r - l + 1)
        return length

        