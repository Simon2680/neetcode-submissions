class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        U: I: String
           O: sub
           C: 
           E: length of subsequence that is greater than s--> return False

              
        P: let use pointers, 
        place a pointer on the s and loop through t until you find the char at where pointer
        at s is 
        once the character is found then  move the pointer
        if you are done with all the characters in s --> True
        otherwise false
           
        I
        """
        pointer =0

        if len(s)>len(t):
            return False
        else:
            for char in range(len(t)):
                if pointer < len(s) and t[char] == s[pointer]:
                    pointer += 1
        return pointer == len(s)

        
        
       

        
      

        