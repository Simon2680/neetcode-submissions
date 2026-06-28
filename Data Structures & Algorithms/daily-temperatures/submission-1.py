class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                if temperatures[stack[-1]] > temperatures[i]:
                    stack.append(i)
                else:
                    while stack and temperatures[stack[-1]] < temperatures[i]:
                        index = stack.pop()
                        res[index] = i-index
                    stack.append(i)
        return res
        
    """
    use stacks:
    create an empty stack
    create a res list
    create a for loop that will pass through all the days:
       if stack is empyty:
          push the day[i] in stack:
        else:
            check if day[-1] from the stack is > day[i], if true:
              push day[i] to the stack
            if not:
                have a while loop to go back and pop everything until day[i] < day[-1] from the stack: --> use a while loop
                  if stack[-1] < days[i]:
                    pop from stack
                    add the distance into res:
                      res[index(popped)] = index(days[i]) - index(popped) 
                  after reaching where stack[-1] > day[i]:
                    stop and push day[i]

                    process continue
        return res

                   
               
                

    """
    


        