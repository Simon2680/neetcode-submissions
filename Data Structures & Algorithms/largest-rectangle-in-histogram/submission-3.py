class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        create a helper method to find the nse
        create a helper method to find the pse
        create max
        loop through the list of heights and calculates newmax = height[i] * (nse-pse-1)
        update max
        return max


        
        """
        """
        if stack
        """
        def nse(heights):
            #return res
            res = [0] *len(heights)
            stack = []
            for i in range(len(heights)-1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                res[i] = stack[-1] if stack else len(heights)
                stack.append(i)
            return res
        def pse(heights):

            res = [0] *(len(heights))
            stack = []
            for i in range(len(heights)):
                while stack and heights[stack[-1]]>= heights[i]:
                    stack.pop()
                res[i] = stack[-1] if stack else -1
                stack.append(i)
            return res
        nsee = nse(heights)
        psee = pse(heights)
        maxx = 0
        for i in range(len(heights)):
            maxx = max(maxx, heights[i]*(nsee[i]-psee[i]-1))
        return maxx


            



              
            

        