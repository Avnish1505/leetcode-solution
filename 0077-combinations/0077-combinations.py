class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def backtrack(start, comb):
            # Base Case: Jab combination size k ke barabar ho jaye
            if len(comb) == k:
                res.append(comb.copy()) # Copy append karna zaroori hai!
                return
            
            # Start se lekar n tak explore karo
            for i in range(start, n + 1):
                # Choose
                comb.append(i)
                # Explore (i + 1 se aage badho taaki order duplicates na ho)
                backtrack(i + 1, comb)
                # Unchoose (Backtrack)
                comb.pop()
                
        backtrack(1, [])
        return res