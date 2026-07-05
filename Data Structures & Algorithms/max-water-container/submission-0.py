class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r:
            detHeight = min(heights[l], heights[r])
            area = (r - l) * detHeight
            maxArea = max(maxArea, area)

            if detHeight == heights[l]:
                l += 1
            else:
                r -= 1
        return maxArea

        