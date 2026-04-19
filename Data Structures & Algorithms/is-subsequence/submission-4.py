class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        U: I: String
           O: sub
           C: 
           E: length of subsequence that is greater than s--> return False

              
        P: compare indices
        I
        """
        if len(s) > len(t):
            return False
        for char in s:
            if char not in t:
                return False
        count = 0
        pointer = 0
        for char in s:
            for i in range(pointer, len(t)):
                if char == t[i]:
                    count += 1
                    pointer = i+1
                    break
        return count == len(s)
            
            
            
       

        
      

        