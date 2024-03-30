from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)

        left = 0
        maxlength = 0

        for right in range(len(s)):
            d[s[right]]+=1
            
            while(d[s[right]]>1):
                d[s[left]]-=1
                left+=1

            

            length = right-left+1
            maxlength = max(length, maxlength)
        return maxlength
