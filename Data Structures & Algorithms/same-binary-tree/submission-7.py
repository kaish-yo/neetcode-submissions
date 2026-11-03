# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def trees_to_list(tree_node: TreeNode) -> list[int|None]:
            queue = deque([tree_node])
            nodes = [tree_node.val if tree_node else None]
    
            while queue:
                curr = queue.popleft()
                if not curr:
                    break
                
                nodes.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                    nodes.append(curr.left.val)
                else:
                    nodes.append(None)
                
                if curr.right:
                    queue.append(curr.right)
                    nodes.append(curr.right.val)
                else:
                    nodes.append(None)
            
            return nodes
        

        return trees_to_list(p) == trees_to_list(q)
            