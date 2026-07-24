class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tkn in tokens:
            match tkn:
                case "+":
                    a,b = stack.pop(), stack.pop()
                    stack.append(b + a)
                case "*":
                    a,b = stack.pop(), stack.pop()
                    stack.append(b*a)
                case "/":
                    a,b = stack.pop(), stack.pop()
                    stack.append(int(b/a))

                case "-":
                    a,b = stack.pop(), stack.pop()
                    stack.append(b - a)
                case _:
                    stack.append(int(tkn))
        return stack[-1]
        