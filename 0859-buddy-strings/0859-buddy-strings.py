class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Step 1: Length check
        if len(s) != len(goal):
            return False
            
        # Step 2: Case 1 - Strings already identical
        if s == goal:
            # Agar duplicate characters hain, toh unhe swap karke string same rahegi
            return len(set(s)) < len(s)
            
        # Step 3: Case 2 - Strings are different
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                
        # Swap tabhi valid hoga jab exact 2 positions par difference ho aur cross-character match karein
        return (
            len(diff) == 2 and 
            s[diff[0]] == goal[diff[1]] and 
            s[diff[1]] == goal[diff[0]]
        )