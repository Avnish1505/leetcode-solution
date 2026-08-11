class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # O(1) lookups ke liye set banao
        longest_streak = 0
        
        for n in num_set:
            # Check karo agar 'n' ek sequence ka starting point hai
            if (n - 1) not in num_set:
                current_num = n
                current_streak = 1
                
                # Consecutive numbers count karte jao
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                    
                # Maximum streak update karo
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak