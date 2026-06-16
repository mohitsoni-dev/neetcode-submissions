class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            if stack:
                warmer = stack[-1][0]
                warmer_idx = stack[-1][1]

                if warmer > temp:
                    res[i] = warmer_idx - i
                else:
                    res[i] = 0
            else:
                res[i] = 0
            
            
            stack.append((temp, i))
        
        return res

"""
 tem = [30,38,30,36,35,40,28]
 res = [  ,  ,  ,  , 1, 0, 0]
                  i

stack = [(40, 5), (35, 4)]
"""