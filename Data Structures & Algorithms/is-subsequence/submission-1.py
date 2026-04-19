class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Edge case: an empty s is always a subsequence
        if not s:
            return True
            
        s_pointer = 0
        
        # We only iterate through t once
        for t_char in t:
            # If the characters match, we move to the next char in s
            if s_pointer < len(s) and t_char == s[s_pointer]:
                s_pointer += 1
        
        # If we reached the end of s, all characters were found in order
        return s_pointer == len(s)