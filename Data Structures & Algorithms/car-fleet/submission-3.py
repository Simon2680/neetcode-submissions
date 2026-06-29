class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        use stack
        create a hasmap that connects postion with time
        sort the hasmap , key = position, decreasing

        loop from the hasmap:
            if stack is empty:
                put the the distance there
            else:
                find the time of stack[-1]
                time of current position
                compare stack[-1] and current position: 
                if current's time >= stack[time] --> fleet, do nothing
                else:
                    add the position on the stack

        return len(stack)

        """

        stack = []
        hasmap = {}
        for i in range(len(position)):
            hasmap[position[i]] = (target-position[i])/speed[i]
        
        # sort the map
        Shasmap = dict(sorted(hasmap.items(), reverse = True))
        for key in Shasmap:
            if not stack or stack[-1] < Shasmap[key]:
                stack.append(Shasmap[key])
           
        return len(stack)





       
        