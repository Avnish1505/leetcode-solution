class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Invalid Cases
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0
            
        subset_target = (target + total_sum) // 2
        
        # dp[i] store karega sum 'i' banane ke total ways
        dp = [0] * (subset_target + 1)
        dp[0] = 1  # 0 sum banane ka 1 way hota hai (kuch mat uthao)
        
        for num in nums:
            # 0/1 Knapsack ke liye loop ko peeche se chalao
            for i in range(subset_target, num - 1, -1):
                dp[i] += dp[i - num]
                
        return dp[subset_target]