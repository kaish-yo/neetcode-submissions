# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        q = deque([root])

        while len(q) >= 1:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    if curr.left:
                        q.append(curr.left)
                        level.append(curr.left.val)
                    if curr.right:
                        q.append(curr.right)
                        level.append(curr.right.val)
            if len(level) >= 1:
                res.append(level[-1])
        
        return res
