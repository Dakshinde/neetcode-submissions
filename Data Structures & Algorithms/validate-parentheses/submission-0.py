class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")" : "(" , "}" : "{" , "]" : "["}

        for char in s :
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(char)

        # If the stack is empty, 'not stack' evaluates to True (Valid!)
        # If the stack still has leftover elements, 'not stack' evaluates to False (Invalid!)
        return not stack