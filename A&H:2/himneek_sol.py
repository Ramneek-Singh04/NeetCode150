class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        copy_dict = {}
        for i in s:
            if i in my_dict:
                my_dict[i] +=1
            else:
                my_dict[i] = 1
        for i in t:
            if i in copy_dict:
                copy_dict[i] +=1
            else:
                copy_dict[i] = 1
        if copy_dict == my_dict:
            return True
        else:
            return False


        
