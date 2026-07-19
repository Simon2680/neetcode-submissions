from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        l
        A A A B A B B
                  r 
        grow:
          populate chars in dictionary
        while invalid: if len(window)-highfreq>k:
            move l until valid again.
            check the s[l]:
               decrement it in the dict
           

        """
        r, l , len_window, high_freq = 0,0,0,0
        hashmap =defaultdict(int)
        max_len = 0
        for r in range(len(s)):
            hashmap[s[r]]+=1
            len_window = r-l+1
            #find high_freq char
            high_freq = max(high_freq, max(list(hashmap.values())))

            while (len_window - high_freq)>k:
                hashmap[s[l]] -=1
                l+=1
                len_window = r-l+1
                
                
                high_freq = max(high_freq, max(list(hashmap.values())))
            max_len = max(max_len, (r-l+1))
        return max_len
            
                


            

        