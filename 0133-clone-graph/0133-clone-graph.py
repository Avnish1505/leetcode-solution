"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        
        old_to_new = {}
        
        def dfs(curr_node):
            if not curr_node:
                return None
                
            # Agar ye node pehle hi clone ho chuka hai, toh purana clone hi return kar do
            if curr_node in old_to_new:
                return old_to_new[curr_node]
                
            # 1. Naya node banao bina neighbors ke
            copy = Node(curr_node.val)
            old_to_new[curr_node] = copy
            
            # 2. Purane node ke saare neighbors par jao
            for neighbor in curr_node.neighbors:
                # Naye node ke neighbors list mein clone kiya hua neighbor append karo
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)
        """
        :type node: Node
        :rtype: Node
        """
        