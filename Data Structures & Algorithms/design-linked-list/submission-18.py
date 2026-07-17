class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            return self.head.val
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val


    def addAtHead(self, val: int) -> None:
        new_head = LinkNode(val=val)
        new_head.next = self.head
        self.head = new_head
        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_tail = LinkNode(val=val)
        if self.size == 0:
            self.head = new_tail
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_tail

        self.size += 1
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val=val)
        elif index == self.size:
            self.addAtTail(val=val)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            
            new_node = LinkNode(val=val)
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1
        return


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            
            curr.next = curr.next.next
            
        self.size -= 1
        return