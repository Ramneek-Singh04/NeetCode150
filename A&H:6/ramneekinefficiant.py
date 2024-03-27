#O(n^2)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        number = 1
        for i in range(len(nums)):
            myList = list(nums)
            myList.remove(myList[i])
            for i in myList:
                number *= i
            solution.append(number)
            number = 1
        return solution
