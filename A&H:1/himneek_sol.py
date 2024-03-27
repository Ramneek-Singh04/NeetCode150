class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_dict = {}
        for i in nums:
            if i in number_dict:
                return True
            else:
                number_dict[i] = 1
