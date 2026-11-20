# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}   # 値 → inorder の位置
        self.p = 0                                    # preorder の読み取り位置

        def build(lo: int, hi: int) -> Optional[TreeNode]:   # inorder[lo..hi] の範囲で木を作る
            if lo > hi:
                return None
            val = preorder[self.p] # preorder を前から1つずつ消費
            self.p += 1       
            root = TreeNode(val)
            k = pos[val]
            root.left  = build(lo, k - 1)             # 左を先に作る(preorder の順番どおり)
            root.right = build(k + 1, hi)
            return root

        return build(0, len(inorder) - 1)