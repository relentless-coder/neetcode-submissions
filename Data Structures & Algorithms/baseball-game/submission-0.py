class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = "+DC"
        stack = []
        for op in operations:
            if op in ops:
                match op:
                    case '+':
                        if stack:
                            a, b = stack.pop(), stack.pop()
                            stack.extend([b, a, a + b])
                    case 'D':
                        if stack:
                            stack.append(2*stack[-1])
                    case 'C':
                        if stack:
                            stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)


        