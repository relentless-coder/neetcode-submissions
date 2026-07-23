class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            match op:
                case "+":
                    if stack:
                        a, b = stack[-1], stack[-2]
                        stack.append(a + b)
                case "D":
                    if stack:
                        stack.append(2 * stack[-1])
                case "C":
                    if stack:
                        stack.pop()
                case _:
                    stack.append(int(op))
        return sum(stack)
