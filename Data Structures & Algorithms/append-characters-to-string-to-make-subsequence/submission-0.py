class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i, j = 0, 0
        while j<len(s) and i<len(t):
            if s[j] == t[i]:
                i+= 1
            j += 1
        return len(t) - i
        