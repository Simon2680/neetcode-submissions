class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R

        while L <= R:
            mid = (L + R) // 2

            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(float(pile) / mid)

            if timeTaken <= h:
                res = mid
                R = mid - 1
            else:
                L = mid + 1

        return res



        