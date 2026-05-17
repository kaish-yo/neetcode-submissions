class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        else:
            new_head = head
        
        head.next = None

        return new_head