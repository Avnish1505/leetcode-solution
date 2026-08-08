# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Helper function jo tree ke saare leaf nodes collect karta hai
        def get_leaves(root):
            leaves = []
            
            def dfs(node):
                if not node:
                    return
                # Leaf node check: Agar dono child None hain
                if not node.left and not node.right:
                    leaves.append(node.val)
                    return
                
                dfs(node.left)
                dfs(node.right)
                
            dfs(root)
            return leaves
            
        # Dono trees ke leaf sequences compare karo
        return get_leaves(root1) == get_leaves(root2)