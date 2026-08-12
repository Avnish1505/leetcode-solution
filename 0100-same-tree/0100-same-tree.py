# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Base Case: Dono nodes null hain
        if not p and not q:
            return True
            
        # 2. Base Case: Ek null hai aur ek non-null (Structure mismatch)
        if not p or not q:
            return False
            
        # 3. Value mismatch check
        if p.val != q.val:
            return False
            
        # 4. Left aur Right subtrees dono match hone chahiye
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)