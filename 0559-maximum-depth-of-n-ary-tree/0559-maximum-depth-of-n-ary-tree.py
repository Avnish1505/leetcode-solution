"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Base Case: Agar tree khali hai
        if not root:
            return 0
            
        # Agar current node ke koi children nahi hain (Leaf node)
        if not root.children:
            return 1
            
        # Saare children ki depth nikaalo aur max find karo
        max_child_depth = max(self.maxDepth(child) for child in root.children)
        
        # Current node ko count karne ke liye 1 add karo
        return 1 + max_child_depth