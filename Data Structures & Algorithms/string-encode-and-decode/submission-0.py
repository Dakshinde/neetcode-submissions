class Solution:

    def encode(self, strs: List[str]) -> str:
        str_final = []
        for i in strs:
            str_final.append(str(len(i)) + "#" + i)
        return "".join(str_final)

    def decode(self, s: str) -> List[str]:
        i = 0
        lis1 = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j +1
            number = int(s[i:j])
            word = s[j+1:j+1+number]
            i = number + 1 + j
            lis1.append(word)
        
        return lis1

                            
