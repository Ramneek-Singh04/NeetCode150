class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = s.lower()
        resString = ""
        for char in new_str:
            if char.isalnum():
                resString += char
        strLen = len(resString)
        for i in range(strLen // 2):
            Pa = resString[strLen - i - 1]
            Pb = resString[i]
            if Pa != Pb:
                return False 
        return True 
