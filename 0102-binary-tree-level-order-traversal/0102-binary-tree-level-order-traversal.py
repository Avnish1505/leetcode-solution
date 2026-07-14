# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base Case: Agar tree khali hai toh empty list return karo
        if not root:
            return []
            
        result = []
        queue = collections.deque([root]) # Queue ko root se initialize kiya
        
        while queue:
            level_size = len(queue) # Current level par kitne nodes hain
            current_level = []
            
            # Is loop se hum current level ke saare nodes ko ek saath process karenge
            for _ in range(level_size):
                node = queue.popleft() # Queue ke aage se node nikaala
                current_level.append(node.val)
                
                # Agar left child hai, toh use queue mein daalo
                if node.left:
                    queue.append(node.left)
                # Agar right child hai, toh use queue mein daalo
                if node.right:
                    queue.append(node.right)
            
            # Poora level process hone ke baad use final result mein add karo
            result.append(current_level)
            
        return result
        