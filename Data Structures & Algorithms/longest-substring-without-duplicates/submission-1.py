class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        char_set = set()
        max_len = 0

        for j in range(len(s)):
            while s[j] in char_set:
                char_set.discard(s[i])
                i += 1
            
            char_set.add(s[j])

            max_len = max(max_len,(j - i + 1))
            print(max_len)

        return max_len
