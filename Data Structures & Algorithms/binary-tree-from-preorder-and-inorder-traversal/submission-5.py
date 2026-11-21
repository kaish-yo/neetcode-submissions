# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        self.p = 0

        def build(lo, hi):
            if lo > hi:
                return

            val = preorder[self.p]
            self.p += 1
            k = pos[val]

            root = TreeNode(val)
            root.left = build(lo, k - 1)
            root.right = build(k + 1, hi)
            return root
        
        return build(0, len(inorder) - 1)

             
        