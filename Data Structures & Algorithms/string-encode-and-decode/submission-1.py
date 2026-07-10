class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        put length of the word befor it and a delimiter next to the length
        then add the actual word

        """
        encoded = ""
        for word in strs:
            encoded += f"{len(word):03}{word}"
        return encoded

    def decode(self, s: str) -> List[str]:

        """
        check for the first characters before heating #
        put the n characters next # into a word that you will append to the result
        use pointers
 
        """

        decoded = []
        curIdx = 0
       
        while curIdx < len(s):
            str_root = curIdx + 3
            ln = int(s[curIdx : str_root])
            curIdx =  str_root + ln # advance the pointer
            decoded.append(s[ str_root : curIdx ])

        return decoded


            

            
        
        

      

        





    
