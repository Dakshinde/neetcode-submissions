class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i<j:
            current_n = numbers[i] + numbers[j]

            if current_n == target:
                return [i+1,j+1]
            elif current_n < target:
                i = i + 1
            else:
                j = j - 1
        
        return [] # O(n) time and O(1) space