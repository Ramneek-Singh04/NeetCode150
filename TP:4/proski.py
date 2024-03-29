class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        max1 = 0

        while(left < right):
            area = min(height[left], height[right]) * (right-left)
            max1 = max(max1, area)
            
            if(height[left]< height[right]):
                left+=1
            elif height[right]< height[left]:
                right-=1
            else:
                left+=1
                right-=1
        return max1
            
            








