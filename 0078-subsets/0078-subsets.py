class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def backtrack(i):
            # Base Case: Agar hum array ke aakhir tak pahunch gaye
            if i >= len(nums):
                res.append(subset.copy()) # Copy lena zaroori hai!
                return
            
            # Option 1: nums[i] ko include karo
            subset.append(nums[i])
            backtrack(i + 1)
            
            # Option 2: Backtrack karo (nums[i] ko hata do)
            subset.pop()
            
            # Option 3: nums[i] ko exclude karke aage badho
            backtrack(i + 1)
            
        backtrack(0)
        return res
        