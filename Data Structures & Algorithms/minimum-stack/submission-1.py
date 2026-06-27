class MinStack:

    def __init__(self):
        self.stack = [] 
        #Writing stack = [] creates a temporary variable that vanishes the second the function finishes running.
        # else NameError: name 'stack' is not defined
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_stack:
            minn = min(self.min_stack[-1] , val)
            self.min_stack.append(minn)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
