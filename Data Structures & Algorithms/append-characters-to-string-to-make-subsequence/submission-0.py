class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        U: I: two strings
           O: integer that represent minimum jumber of chars needed to make t the subsequence of s

           C: 
           E: t = s --> return 0
              if t is already a subsequence --> return 0
        P: create a pointer to move through s checking for char from t and 
           pointer to move through t

           if char in s == char i t: 
               move pointer of s to that char
               move pointer of t by 1

            if we reache the end and both pointers == their corresponding 
            string len --> return 0 

            elif we reache the end of s and we haven't reached the end of t:
                return len(t)-tPointer
            
        I
        """
        tPointer = 0
        

        
        for i in range(len(s)):
            if tPointer<len(t):
                if s[i] == t[tPointer]:
                    tPointer +=1
                    
        
        return len(t)-tPointer
                
                   




        