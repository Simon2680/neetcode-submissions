class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        sm = sum(arr[:k])
        ans = 1 if sm >= target else 0

        for R in range(k, len(arr)):
            sm += arr[R] - arr[R-k]
            if sm >= target:
                ans += 1

        return ans
        