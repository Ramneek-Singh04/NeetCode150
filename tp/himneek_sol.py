class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        resultarr = []
        leftPointer = 0
        rightPointer = len(numbers)-1
        sumval = 0
        checker = False
        while checker != True:
            left = numbers[leftPointer]
            right = numbers[rightPointer]
            sumval = left + right
            if sumval > target:
                rightPointer -= 1
            elif sumval < target:
                leftPointer += 1
            elif sumval == target:
                checker = True
        resultarr.append(leftPointer +1)
        resultarr.append(rightPointer + 1)
        return resultarr
