# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.prev = None
        
        def inorder(node):
            if not node:
                return
                
            # 1. Left subtree visit karo
            inorder(node.left)
            
            # 2. Current node process karo
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val  # Current node ko 'prev' bana do agli node ke liye
            
            # 3. Right subtree visit karo
            inorder(node.right)
            
        inorder(root)
        return self.min_diff