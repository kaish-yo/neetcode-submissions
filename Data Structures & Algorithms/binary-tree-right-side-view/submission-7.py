# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = list()
        levels = list()

        if root:
            res.append(root.val)
            levels.append(root)
        
        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()

                if not curr:
                    continue

                if curr.left:
                    q.append(curr.left)
                    level.append(curr.left.val)

                if curr.right:
                    q.append(curr.right)
                    level.append(curr.right.val)
            
            if level:
                res.append(level[-1])

        return res
                