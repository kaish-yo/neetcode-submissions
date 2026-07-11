class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if isinstance(val, int):
            self.stack.append(val)
            print(self.stack)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
