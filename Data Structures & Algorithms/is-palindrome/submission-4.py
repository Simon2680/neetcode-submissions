class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        remove all the spaces in the string
        read the string in reverse 
        return if both strings are equal

        """


        rem = list(s.replace(" ", "").lower())
        rem2 = rem.copy()
        for i in range(len(rem2)):
            if not rem2[i].isalpha() and not rem2[i].isdigit():
               rem.remove(rem2[i])

        rev = rem[::-1]
        return rev == rem
       

        