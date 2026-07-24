class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Step 1: Length check
        if len(s) != len(goal):
            return False
            
        # Step 2: Check if goal is a substring of (s + s)
        return goal in (s + s)