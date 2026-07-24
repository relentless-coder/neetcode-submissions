class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tkn in tokens:
            if tkn == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif tkn == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif tkn == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            elif tkn == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            else:
                stack.append(int(tkn))
        return stack[-1]
