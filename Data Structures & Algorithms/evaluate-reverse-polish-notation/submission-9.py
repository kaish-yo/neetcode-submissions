class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in ops:
                second, first = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(first + second)
                if token == "-":
                    stack.append(first - second)
                if token == "*":
                    stack.append(first * second)
                if token == "/":
                    stack.append(int(first / second))   
            else:
                stack.append(int(token))
        
        return stack[-1]