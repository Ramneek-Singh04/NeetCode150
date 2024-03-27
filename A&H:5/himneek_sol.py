class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        returnList = []
        
        for i in nums:
            if i in myDict:
                myDict[i] +=1
            else:
                myDict[i] = 1
              
        for i in range(k):
            returnList.append(max(myDict, key=myDict.get))
            myDict[(max(myDict, key=myDict.get))] = 0
        return returnList
        
