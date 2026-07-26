class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] store karega 'i' amount banane ke total combinations
        dp = [0] * (amount + 1)
        
        # Base Case: 0 amount banane ka sirf 1 hi tarika hota hai (kuch mat do)
        dp[0] = 1
        
        # 🌟 GOLDEN RULE: Coin ka loop hamesha BAAHAR hoga (Combinations ke liye)
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                
        return dp[amount]