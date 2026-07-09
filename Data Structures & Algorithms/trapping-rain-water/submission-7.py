class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
    
        max_right = [0] * n
    
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
    
        water = 0
        max_left = 0
    
        for i in range(1, n):
            max_left = max(max_left, height[i - 1])
            water += max(0, min(max_left, max_right[i]) - height[i])
    
        return water

        