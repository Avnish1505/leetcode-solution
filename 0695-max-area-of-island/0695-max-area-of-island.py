class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r, c):
            # Base Case: Agar boundaries se baahar hain ya paani (0) hai
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            # Current land ko visit mark karo (sink the land)
            grid[r][c] = 0
            
            # Chaaron directions mein explore karo aur area jodte jao
            return (1 + 
                    dfs(r + 1, c) +  # Down
                    dfs(r - 1, c) +  # Up
                    dfs(r, c + 1) +  # Right
                    dfs(r, c - 1))   # Left

        # Pure grid par traverse karo
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # Agar naya island mila, toh uska area nikaalo aur max update karo
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area
        