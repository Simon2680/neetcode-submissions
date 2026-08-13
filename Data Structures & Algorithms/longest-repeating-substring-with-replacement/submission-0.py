class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unq_chars = {}
        win_len = 0
        l_ptr = 0
        res = 0

        for char in s:

            unq_chars[char] = unq_chars.get(char, 0) + 1
            win_len += 1

            # when replacements needed > allowed:
            # reduce size of window
            while win_len - max(unq_chars.values()) > k and l_ptr < len(s):
                unq_chars[s[l_ptr]] = max(unq_chars[s[l_ptr]]-1, 0)
                win_len -= 1
                l_ptr += 1

            res = max(res, win_len)
        return res
            


                
            

        

            
            

