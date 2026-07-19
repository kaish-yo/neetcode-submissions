class LinkNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = LinkNode(val = homepage) # pointer

    def visit(self, url: str) -> None:
        new_node = LinkNode(val=url)
        new_node.prev = self.head
        self.head.next = new_node
        # Move the pointer forward
        self.head = self.head.next

    def back(self, steps: int) -> str:
        if not self.head.prev:
            return self.head.val

        for _ in range(steps):
            self.head = self.head.prev
            if self.head.prev == None:
                break

        return self.head.val
        
    def forward(self, steps: int) -> str:
        if not self.head.next:
            return self.head.val
    
        for _ in range(steps):
            self.head = self.head.next
            if self.head.next == None:
                break
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)