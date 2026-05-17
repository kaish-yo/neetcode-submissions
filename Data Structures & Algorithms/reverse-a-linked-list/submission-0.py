# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            temp = curr.next # 元のheadのnextを退避
            ### 逆順処理
            curr.next = prev 
            prev = curr
            ###
            curr = temp # 次のheadにポインターを移動
        return prev # 逆順後の終端を返す

        