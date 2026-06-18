class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        pre_stack = []
        pre = [-1] * n

        for i in range(n):
            while pre_stack and heights[pre_stack[-1]] >= heights[i]:
                pre_stack.pop()
            
            if pre_stack:
                pre[i] = pre_stack[-1]
            pre_stack.append(i)
        suff = [n] * n
        pre_stack = []

        for i in range(n-1, -1, -1):
            while pre_stack and heights[pre_stack[-1]] >= heights[i]:
                pre_stack.pop()
            
            if pre_stack:
                suff[i] = pre_stack[-1]
            pre_stack.append(i)
        
        ans = 0

        for i in range(n):
            left = pre[i]
            right = suff[i]

            width = right - left - 1
            area = width * heights[i]
            ans = max(ans, area)


        return ans



