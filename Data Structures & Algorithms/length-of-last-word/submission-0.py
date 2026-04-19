class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        news = s.strip()
        lis = list(news.split())
        return len(lis[-1])
        