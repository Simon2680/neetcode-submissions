class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        remove all the spaces in the string
        read the string in reverse 
        return if both strings are equal

        """


        # rem = list(s.replace(" ", "").lower())
        # rem2 = rem.copy()
        # for i in range(len(rem2)):
        #     if not rem2[i].isalpha() and not rem2[i].isdigit():
        #        rem.remove(rem2[i])

        # rev = rem[::-1]
        # return rev == rem

        
        
        news = []
        for i in range(len(s)):
            if s[i].isalnum():
                news.append(s[i].lower())
        leftp= 0
        rightp = len(news)-1


        while leftp <= rightp:
            if news[rightp] !=news[leftp]:
                return False
            leftp +=1
            rightp -=1
        return True



       

        