class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxprofit = 0
        min1 = 1000000
        max1 = -1000000

        for i in range(len(nums)):
            if(nums[i] < min1):
                min1 = nums[i]
            maxprofit = max(maxprofit, nums[i]-min1)

        return maxprofit

