class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i, op in enumerate(operations):
            print(res)
            try: 
                op = int(op)
                res.append(op)
            except:
                if op == "+":
                    res.append(res[-1] + res[-2])
                elif op == "C":
                    res.pop()
                elif op == "D":
                    res.append(res[-1] * 2)
        return sum(res)