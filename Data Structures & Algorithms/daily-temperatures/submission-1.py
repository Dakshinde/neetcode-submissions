class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n # initially all are zero
        stack = []

        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                old_index = stack.pop()
                result[old_index] = i - old_index # or simply  result[stack[-1]] = i - stack.pop() 
            
            stack.append(i)
        
        return result