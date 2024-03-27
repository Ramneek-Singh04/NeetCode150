class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = nums
        new_nums.sort()
        print(new_nums)
        counter = 1
        new_max = 0
        if len(new_nums) == 0:
            return 0
        for i in range(len(new_nums)-1):
            if (new_nums[i]+1) == new_nums[i+1]:
                counter +=1
            elif (new_nums[i] == new_nums[i+1]):
                continue
            else:
                if counter > new_max:
                    new_max = counter
                counter = 1
        if counter > new_max:
            new_max = counter
        return new_max
        
