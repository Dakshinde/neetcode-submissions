class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        import operator
        # Maps the string token to its corresponding function
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b) # Handles our custom truncate-toward-zero rule!
        }

        stack = []

        for i in tokens:
            if i in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                result = ops[i](num1,num2)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack.pop()