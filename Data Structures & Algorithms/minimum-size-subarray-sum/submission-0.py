class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        minLen = float('inf')
        curSum = 0
        for R in range(len(nums)):
            curSum += nums[R]

            while curSum >= target:
                minLen = min(minLen, R - L + 1)
                curSum -= nums[L]
                L += 1

        return minLen if minLen != float('inf') else 0
