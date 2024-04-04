class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ssl = 0
        substring = ''
        for letter in s:
            if letter not in substring:
                substring += letter
            else:
                prevcounter = len(substring)
                ssl = max(ssl, prevcounter)
                index = substring.index(letter)
                substring = substring[index + 1:] + letter
        ssl = max(len(substring), ssl)
        return ssl
