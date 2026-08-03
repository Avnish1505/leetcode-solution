# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(node, path):
            if not node:
                return
                
            # Current node ki value path mein append karo
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)
                
            # Base Case: Agar leaf node hai, toh path result mein add kar do
            if not node.left and not node.right:
                result.append(path)
                return
                
            # Recursive steps: Left aur Right subtree check karo
            dfs(node.left, path)
            dfs(node.right, path)
            
        dfs(root, "")
        return result