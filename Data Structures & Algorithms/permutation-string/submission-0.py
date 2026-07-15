from collections import Counter
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1hasmap = Counter(s1)
        temps1 = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            if r-l < len(s1):
                temps1[s2[r]] +=1
            else:
                if s1hasmap == temps1:
                    return True
                else:
                    temps1[s2[l]] -=1
                    if temps1[s2[l]] == 0:
                        del temps1[s2[l]]
                    l +=1
                    temps1[s2[r]] +=1
        return s1hasmap == temps1
                    
                    
                
        
        
        
        
        
        
            
                
            
                
                    
                
                    
                    
                        
                    
        
        
        
        
    #     """
      
               
    #           l               
    #   s2 = "e i d b a o o o"
    #               r  
                   
         
        
    #     """
    #     """
    #     create s1 hashmap ={a:1, b:1}
    #     temps1 = {}
    #     l = 0
    #     for loop to move r:
    #         if r-l < len(s1):
    #             populate temps1[r]
    #         else:
    #             check if s1 == temps1
    #             if True--> True
    #             else:
    #                 decrement temps1[l] by 1
    #                 check if it the value is 0:
    #                 if true--> remove the l in the temps1
    #                 incerement l by 1
    #     return false
        
    #     """
       