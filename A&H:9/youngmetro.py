class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if(len(nums)==0):
            return 0
        numset = set(nums)
        maxlength = 1

        for n in numset:
            if(n-1 not in numset):
                length = 1
                while(n + length in numset):
                        length+=1
                        maxlength = max(length, maxlength)
        return maxlength
            
