class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = {"+": lambda x, y: x+y, "-": lambda x, y: x-y, "*": lambda x, y: x*y, "/": lambda x, y: int(x/y)}

        stack = []

        for c in tokens:
            if c in symbols:
                val2 = stack.pop()
                val1 = stack.pop()

                method = symbols.get(c)

                ans = method(val1, val2)
                stack.append(ans)
            else:
                stack.append(int(c))
        
        return stack.pop()


"""
[22]
"""