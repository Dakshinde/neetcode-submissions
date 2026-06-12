class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [i.lower() for i in s if i.isalnum()] # isalnum means is it alphabetical or numeric
        print(cleaned)

        joined_text = "".join(cleaned)
        print(joined_text)

        i = 0
        j = len(joined_text) - 1

        while i<j:
            if joined_text[i] == joined_text[j]:
                i = i + 1
                j = j - 1
            else:
                return False
        return True