class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        for i in range(n):
            for j in range(i+1 , n):
                if temperatures[j] > temperatures[i]:
                    val = j - i 
                    result[i] = val
                    break 
        return result
        