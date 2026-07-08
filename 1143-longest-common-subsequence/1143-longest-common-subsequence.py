class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. Ek 2D Grid banao jisme shuru mein sab 0 ho
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 2. Bottom-up tarike se matrix ko peeche se bharo
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Case 1: Agar character match kar gaya
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # Case 2: Agar match nahi kiya, toh max nikaalo
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                    
        # 3. Top-left cell (0,0) mein hamara final answer hoga
        return dp[0][0]
        