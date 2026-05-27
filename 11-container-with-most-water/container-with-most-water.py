class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            
            diff = right - left
            
            if height[left] > height[right]:
                temp_area = height[right] * diff
                right -= 1
            else:
                temp_area = height[left] * diff
                left += 1

            max_area = max(max_area, temp_area)
        
        return max_area