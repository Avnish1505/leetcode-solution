class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Step 1: Array ko sort karo
        nums.sort()
        
        count = 0
        left = 0
        right = len(nums) - 1
        
        # Step 2: Two Pointers lagao
        while left < right:
            if nums[left] + nums[right] < target:
                # Agar dono ends ka sum target se chhota hai
                # Toh beech ke saare numbers bhi left ke saath valid pair banayenge
                count += (right - left)
                left += 1
            else:
                # Sum bada ho gaya, chhota karne ke liye right ko peeche laao
                right -= 1
                
        return count