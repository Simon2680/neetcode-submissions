class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        area =0
        use two pointers right and left at both ends
        use a while loop that wil check if the pointers hasn't met yet
        find the width --> right-left
        find the height == min(height[right], height[left])
        find area
        update area if it's grater than the previous one--> use max
        then: move the pointers:
             move the one with height[pointer] is small
             if they are equal, move any

        return the area

        """
        area = 0
        left = 0
        right = len(heights)-1
        while right > left:
            # find width
            width = right -left
            height = min(heights[right], heights[left])
            area = max(area, height * width)
             # move pointers
            if heights[right] > heights[left]:
                left +=1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left +=1
        return area

        