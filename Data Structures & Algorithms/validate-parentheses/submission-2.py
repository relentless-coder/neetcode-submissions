class Solution:
    def isValid(self, s: str) -> bool:
        close_open_pair = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in close_open_pair:
                if not stack:
                    return False
                if stack.pop() != close_open_pair[char]:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
        