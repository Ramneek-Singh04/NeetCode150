class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        prefix.append(1)
        suffix = []
        suffix = [0]* len(nums)
        suffix[len(nums)-1]=1
        prefixsum = 1
        suffixsum= 1
        res = []
        
        for i in range(1, len(nums)):
            prefixsum*= nums[i-1]
            prefix.append(prefixsum)
        print(prefix)

        for i in range(len(nums)-2, -1,-1):
            suffixsum*= nums[i+1]
            suffix[i]=(suffixsum)
        
        print(suffix)
        for i in range(len(nums)):
            res.append(suffix[i]*prefix[i])
        return res
        


            

