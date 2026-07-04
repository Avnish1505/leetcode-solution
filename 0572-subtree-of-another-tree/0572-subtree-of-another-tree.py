# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            # Note: Agar subRoot bhi None hota toh True hota, par LeetCode par subRoot khali nahi diya jata
            return False
            
        # 2. Agar current node se shuru hone wala tree aur subRoot same hain, toh True
        if self.isSameTree(root, subRoot):
            return True
            
        # 3. Warna check karo ki kya subRoot left ya right child mein se kisi ka subtree hai
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    # Hamaara purana trusty Same Tree helper function
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)