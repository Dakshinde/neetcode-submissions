class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}

        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i] , 0) + 1
        
        print(s1_map)

        window_map = {}

        for j in range(len(s2)):
            right = s2[j]
            window_map[right] = window_map.get(right , 0) + 1 # counts the occurence

            if j >= len(s1):
                left = s2[j - len(s1)] # the first element of slide whole size is greater than len(s1)

                window_map[left] -= 1 
                # reduce count of the element that needs to leave the slide

                # if the removing element count is zero we need to delete it from dictionary
                if window_map[left] == 0 :
                    del window_map[left]
            
            if window_map == s1_map: # if mapped then immediatley return True
                return True
        
        return False # since after whole loop no True was return means no permutation so return False

        