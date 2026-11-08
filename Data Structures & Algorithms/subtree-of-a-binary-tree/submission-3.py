# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.is_same_tree(root, subRoot):
            return True
        
        return (
            (
                self.isSubtree(root.left, subRoot)
            ) or (
                self.isSubtree(root.right, subRoot)
            )
        )
        
    
    def is_same_tree(self, first, second):
        if not first and not second:
            return True
        
        if first and second and first.val == second.val:
            return (
                (
                    self.is_same_tree(first.left, second.left)
                ) and (
                    self.is_same_tree(first.right, second.right)
                )
            )
        
        return False