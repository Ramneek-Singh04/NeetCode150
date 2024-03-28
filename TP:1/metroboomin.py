class Solution:
     def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()


        right = len(s)-1
        left = 0

        while(right > left):
        

            while(s[right].isalnum() is False and right > left):
                right-=1
            while(s[left].isalnum() is False and left <right):
                left+=1
            
            if(s[right]!=s[left]):
                return False
            right-=1
            left+=1
        
        return True
        
