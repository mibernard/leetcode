class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        left, right = 0, len(height) - 1
        
        while right > left: 
            dist = right - left
            maxA = max(maxA, dist * min(height[left], height[right]))        
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxA

#Time: O(n)
