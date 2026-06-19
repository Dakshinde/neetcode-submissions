class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0 
        count_map = {}
        max_len = 0
        most_freq = 0

        for j in range(len(s)):

            count_map[s[j]] = count_map.get(s[j] , 0) + 1

            most_freq = max(most_freq , count_map[s[j]])

            # lub = j - i + 1 # length of window 

            # length of window - most frequent element of slide if greater than k then we terminate
            
            while (j-i+1) - most_freq > k:
                count_map[s[i]] = count_map[s[i]] - 1
                i = i + 1
            
            max_len = max(max_len ,j - i + 1)
            print(max_len)
        
        return max_len