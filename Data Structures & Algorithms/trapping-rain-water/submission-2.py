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


          
        # """
        # if len(height) < 2:
        #     return 0

        # water = 0

        # for i in range(len(height)):
        #     if i ==0:
        #         leftmax =0
        #         rightmax = max(height[i+1::])

        #     elif i == len(height)-1:
        #         rightmax = 0
        #         leftmax = max(height[::i])

        #     else:
        #         leftmax = max(height[::i])
        #         rightmax = max(height[i+1::])
            
        #     Gmin = min(leftmax, rightmax)
        #     units = Gmin-height[i]
        #     if units>0:
        #         water += units
        # return water
        # ############################
        # #O(n) solution
        # """
        # first find the left maxes and put them in the list: use o(n):
        #   create a for loop:
        #   left max of the first number is 0 
        #   creaee a number that will keep the value of current max
        #   compare the value to the new max and update the cuurent max:
        
        #  """

        leftmaxes=[0]
        currmax = 0
        for i in range(len(height)):
            if height[i]>currmax and i!=len(height)-1:
                leftmaxes.append(height[i])
                currmax = height[i] 
            else:
                leftmaxes.append(currmax)
        rightmaxes =[0]
        cmx = 0
        for i in range(len(height)-1,-1, -1):
            if height[i] > cmx and i != 0:
                rightmaxes.append(height[i])
                cmx = height[i]
            else:
                rightmaxes.append(cmx)
        rightmaxes.reverse()

        water = 0

        for i in range(len(height)):
            Gmin = min(leftmaxes[i], rightmaxes[i])
            units = Gmin-height[i]
            if units>0:
                water += units
        return water






















































