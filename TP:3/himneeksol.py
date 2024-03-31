class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resArr = []
        nums.sort()
        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                ThreeSum = nums[i] + nums[left] + nums[right]
                if ThreeSum > 0:
                    right -= 1
                elif ThreeSum < 0:
                    left += 1
                else:
                    templist = []
                    templist.append(nums[i])
                    templist.append(nums[left])
                    templist.append(nums[right])
                    resArr.append(templist)
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
        return resArr
