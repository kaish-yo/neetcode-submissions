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

        next_node = nodes[idx + 1] if idx + 1 < len(nodes) else None

        if idx == 0:
            if len(nodes) <= 1:
                return
            return nodes[1]
        
        nodes[idx - 1].next = next_node
        nodes[idx].next = None

        return nodes[0]

        