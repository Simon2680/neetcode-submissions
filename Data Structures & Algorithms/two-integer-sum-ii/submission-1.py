class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        R = len(numbers) -1

        for L in range(len(numbers)):
            while numbers[L] + numbers[R] > target:
                R = R - 1

            if numbers[L] + numbers[R] == target:
                return [L+1, R+1]

