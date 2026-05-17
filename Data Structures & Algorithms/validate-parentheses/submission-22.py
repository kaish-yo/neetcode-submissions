class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for c in s:
            if stack and c in close_to_open:
                if stack[-1] == close_to_open[c]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        else:
            return False
