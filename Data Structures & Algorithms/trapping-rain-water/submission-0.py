class Solution:
    def trap(self, height: List[int]) -> int:
        """
        o(n) and o(n) space solution
        ##############################
        water = 0
        use a for loop that will  pass once at every number:
          find max at the left
          find max at the right
          find maxG between (maxright, and maxleft)
          find the maxG-cuurent height --> call it units
            if units > 0:
                water+=units

        return water


          
        """
        if len(height) < 2:
            return 0

        water = 0

        for i in range(len(height)):
            if i ==0:
                leftmax =0
                rightmax = max(height[i+1:])

            elif i == len(height)-1:
                rightmax = 0
                leftmax = max(height[0:i])

            else:
                leftmax = max(height[0:i])
                rightmax = max(height[i+1:])
            
            Gmin = min(leftmax, rightmax)
            units = Gmin-height[i]
            if units>0:
                water += units
        return water