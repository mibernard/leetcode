class Solution:
    def maxArea(self, height: List[int]) -> int:
        dist, maxA = 0, 0
        left, right = 0, len(height) - 1
        
        while right > left: 
            dist = right - left
            currA = dist * min(height[left], height[right])
            if currA > maxA:
                maxA = currA
            else:
                if height[left] > height[right]:
                    right -= 1
                else:
                    left += 1
        return maxA

#Time: O(n)
