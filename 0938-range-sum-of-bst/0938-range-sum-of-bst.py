# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
            
        # Case 1: Agar node ki value range se choti hai, toh sirf right mein dhoondho
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
            
        # Case 2: Agar node ki value range se badi hai, toh sirf left mein dhoondho
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
            
        # Case 3: Node range ke andar hai, toh iski val add karo + left & right dono jagah jao
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)