class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        
        # Base Check: Total length match honi chahiye
        if m + n != len(s3):
            return False
            
        # dp[i][j] matrix initialization with False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base Case: Empty strings can form empty s3
        dp[0][0] = True
        
        # 1. First Row fill karo (Jab s1 se kuch nahi liya, sirf s2 use kar rahe hain)
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        # 2. First Column fill karo (Jab s2 se kuch nahi liya, sirf s1 use kar rahe hain)
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            
        # 3. Grid ko fill karo
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Top se match check karo (s1 ka char match)
                from_top = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                # Left se match check karo (s2 ka char match)
                from_left = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                
                dp[i][j] = from_top or from_left
                
        return dp[m][n]