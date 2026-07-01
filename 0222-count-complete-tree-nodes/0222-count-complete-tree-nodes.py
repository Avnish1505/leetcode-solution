# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        # 1. Left height nikalne ke liye function
        def get_left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
            
        # 2. Right height nikalne ke liye function
        def get_right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
            
        lh = get_left_height(root)
        rh = get_right_height(root)
        
        # 3. Agar left aur right height barabar hai (Perfect Binary Tree)
        if lh == rh:
            # 2^lh - 1 bits modification se fast hota hai: (1 << lh) - 1
            return (1 << lh) - 1
            
        # 4. Agar barabar nahi hai, toh recursion lagao
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        