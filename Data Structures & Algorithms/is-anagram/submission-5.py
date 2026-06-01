class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        

        countS = {}
        counT = {}

        for i in s:
            if i not in countS:

                countS[i] = 1
            else:
                countS[i] = countS[i] + 1
        
        for i in t:
            if i not in counT :
                counT[i] = 1
            else:
                counT[i] = counT[i] + 1
        
        return countS == counT