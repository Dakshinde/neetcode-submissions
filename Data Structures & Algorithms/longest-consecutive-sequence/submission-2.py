class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        num_set = set(nums)

        print(num_set)

        longest_streak = 0

        for n in num_set:
            if (n - 1) not in num_set:
                # If (n - 1) is NOT there, 'n' MUST be the start of a sequence!
                start = n
                count = 1

                while (start+1) in num_set:
                    start = start + 1
                    count = count + 1
                
                longest_streak = max(longest_streak, count)
                
        return longest_streak