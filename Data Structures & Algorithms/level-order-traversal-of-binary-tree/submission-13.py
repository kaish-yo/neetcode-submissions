# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root:
            levels.append([root.val])
        q = deque([root])

        while len(q) >= 1:
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
                levels.append(level)
        
        return levels

                    

        
        
        