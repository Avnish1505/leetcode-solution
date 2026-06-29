# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # 1. Agar node khali hai, toh koi path nahi ban sakta
        if not root:
            return False
            
        # 2. Check karo kya yeh ek leaf node hai
        if not root.left and not root.right:
            # Agar leaf node ki value bache hue targetSum ke barabar hai, toh True
            return root.val == targetSum
            
        # 3. Naya target calculate karo current node ki value subtract karke
        new_target = targetSum - root.val
        
        # Left ya Right kisi bhi ek side se true mil jaye toh chalega (OR condition)
        return self.hasPathSum(root.left, new_target) or self.hasPathSum(root.right, new_target)