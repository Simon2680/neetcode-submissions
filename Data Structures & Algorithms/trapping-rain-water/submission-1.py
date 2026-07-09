class Solution:
    def trap(self, height: List[int]) -> int:

        final = 0
        maxRight = [0] * len(height)
        maxLeft = [0] * len(height)
        for i in reversed(range(len(height) - 1)):
            maxRight[i] = max(height[i+1],maxRight[i+1])
        
        for i in range(1,len(height)):
            maxLeft[i] = max(height[i-1],maxLeft[i-1])
            final += max((min(maxRight[i], maxLeft[i]) - height[i]), 0)

        # print(maxLeft)
        # print(maxRight)

        return final

        