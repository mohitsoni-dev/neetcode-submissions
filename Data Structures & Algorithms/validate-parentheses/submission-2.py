class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c not in brackets:
                stack.append(c)
            else:
                opening_bracket = brackets.get(c)
                if not stack or opening_bracket != stack[-1]:
                    return False
                
                stack.pop()
        
        return not stack
