class Solution:
    def validPalindrome(self, s: str) -> bool:
        removed = 0
        l = 0
        r = len(s) - 1

        def is_palindrome(lo, hi):
            while lo <= hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            
            return True

        while l <= r:
            if s[l] != s[r]:
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            
            l += 1
            r -= 1
        
        return True
        