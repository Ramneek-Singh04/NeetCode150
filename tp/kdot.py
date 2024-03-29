class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        x = [0]*2

        left = 0
        right = len(numbers)-1
        middle = len(numbers)//2

        while(left < right):
            sum1 = numbers[left]+numbers[right]

            if(sum1 > target):
                right = right-1

            elif sum1 < target:
                left = left+1
            else:
                x[0]= left+1
                x[1]= right+1
                return x
        
