class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            lis1 = sorted(s)
            lis2 = sorted(t)
            if lis1 == lis2:
                return True
            else:
                return False
        else:
            return False
            
        