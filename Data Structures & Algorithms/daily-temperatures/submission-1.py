class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        
        # for i in range(len(temperatures)):
        #     if (i+1) == len(temperatures):
        #         res.append(0)
        #         continue

        #     counter = 1

        #     while temperatures[i] > temperatures[i+counter]:
        #         counter += 1
        #         if i + counter == len(temperatures):
        #             counter = 0
        #             break
        #     res.append(counter)

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                T, idx = stack.pop()
                res[idx] = (i - idx)
            stack.append([t, i])

        return res
