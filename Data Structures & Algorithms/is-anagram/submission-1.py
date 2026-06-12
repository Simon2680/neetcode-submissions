class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
        hasmap1 = {}
        hasmap2 = {}
        for char in s:
            if char in hasmap1:
                hasmap1[char] += 1
            else:
                hasmap1[char] = 1
        for char in t:
            if char in hasmap2:
                hasmap2[char] += 1
            else:
                hasmap2[char] = 1
        return hasmap1 == hasmap2
    