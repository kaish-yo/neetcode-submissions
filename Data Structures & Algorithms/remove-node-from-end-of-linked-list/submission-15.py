# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        idx = len(nodes) - n

        if idx - 1 >= 0:
            if idx + 1 < len(nodes):
                nodes[idx - 1].next = nodes[idx + 1]
                nodes[idx].next = None
            else:
                nodes[idx - 1].next = None
        else:
            if idx + 1 < len(nodes):
                nodes[idx].next = None
            
            nodes.pop(idx)
                
        return nodes[0] if len(nodes) > 0 else None
            

        