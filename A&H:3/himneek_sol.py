class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_array = []
        for i in nums:
            temp = target - i
            new_nums = nums.copy()
            new_nums.remove(i)
            if temp in new_nums:
                return_array.append(nums.index(i))
                if temp == i:
                    nums[nums.index(i)] = i+1
                return_array.append(nums.index(temp))
                return return_array
                
        
