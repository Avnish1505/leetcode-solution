class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        # Deque mein hum indices store karenge
        dq = deque([0])
        
        for i in range(1, n):
            # 1. Jo index window se bhaar ho gaya (out of k range), use hatao
            if dq[0] < i - k:
                dq.popleft()
                
            # 2. Current index ka max score nikaalo using the front of deque
            dp[i] = nums[i] + dp[dq[0]]
            
            # 3. Deque ko monotonic decreasing rakho (chote scores piche se hatao)
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
                
            # 4. Current index ko queue mein add karo
            dq.append(i)
            
        return dp[-1]