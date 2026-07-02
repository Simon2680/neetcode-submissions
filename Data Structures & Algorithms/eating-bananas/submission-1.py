import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      
    
      #   create a minK 
      minK = max(piles)
      #   create a k list , k = [k for k in range(1, max(h))

      #   r,l pointers
      left,right = 1, max(piles)-1

      #   while loop that will go through all the k values
      while right>=left:
         #     find the mid
         mid = (right+left)//2
         #use the mid values : k[mid] and loop over the piles to calculate the time taken:
         currentK = mid
         #totaTime variable created
         totalTime = 0
         for i in range(len(piles)):
          #time variable that will keep increment
          time = math.ceil(piles[i]/currentK)
          totalTime += time
         if totalTime <= h:
          minK = min(minK, currentK)
          right = mid-1
         else:
          left = mid +1
          
          # go left
         
         
      return minK
    
      

        










      



     


      

      
      #        create a for loop over piles:
      #           remember to ceil the time before adding it to the current totaltime sofar

      #           compare total time and h:
      #           if totaltime >= h:
      #             update minK with k[mid]
      #             <<----- in k
      #           if totaltime <=h:
      #             ---> increase the k go right
      # return minK
      
        