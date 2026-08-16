class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # create maps
        t_map = {}
        for char_t in t:
            t_map[char_t] = t_map.get(char_t, 0) + 1
        
        s_map = {}
        for key in t_map:
            s_map[key] = 0

        res = (0,100001)
        L = R = 0
        required = len(t_map)
        formed = 0

        while R < len(s):
            char = s[R]
            if char in t_map:
                s_map[char] += 1
                if s_map[char] == t_map[char]:
                    formed += 1
            
            while formed == required:
                if (R - L + 1) < (res[1] - res[0] + 1):
                    res = (L, R)
                
                left_char = s[L]
                if left_char in t_map:
                    if s_map[left_char] == t_map[left_char]:
                        formed -= 1
                    s_map[left_char] -= 1
                L += 1

            R += 1
        return "" if res[1] > 100000 else s[res[0]:res[1]+1]