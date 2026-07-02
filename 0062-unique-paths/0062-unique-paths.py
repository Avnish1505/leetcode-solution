class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       # 1. Ek 2D matrix banao jisme saari values shuru mein 1 hon
        # Kyunki pehli row aur pehle col mein hamesha 1 hi unique path hoti hai
        dp = [[1] * n for _ in range(m)]
        
        # 2. Row 1 aur Col 1 se shuru karke baaki cells bharo
        for r in range(1, m):
            for c in range(1, n):
                # Current cell = Upar wala cell + Left wala cell
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
                
        # 3. Bottom-right corner mein hamara answer hoga
        return dp[m-1][n-1] 