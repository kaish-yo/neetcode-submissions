class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]

        stack = []
        for token in tokens:
            if token in ops:
                temp2 = stack.pop()
                temp1 = stack.pop()
                if token == "+":
                    stack.append(temp1 + temp2)
                elif token == "-":
                    stack.append(temp1 - temp2)
                elif token == "*":
                    stack.append(temp1 * temp2)
                elif token == "/":
                    stack.append(int(temp1 / temp2))
            else:
                stack.append(int(token))
        
        return stack[-1]
                    
            