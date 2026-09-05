class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Precompute Suffix Minimums
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        # Step 2: Running Prefix Max check in single pass
        prefix_max = float('-inf')
        
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            
            # Instability Score calculation
            if prefix_max - suffix_min[i] <= k:
                return i
                
        return -1