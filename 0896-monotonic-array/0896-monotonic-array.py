class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        is_increasing = True
        is_decreasing = True
        
        for i in range(len(nums) - 1):
            # Agar purana element agle se bada hai, toh increasing nahi ho sakta
            if nums[i] > nums[i + 1]:
                is_increasing = False
                
            # Agar purana element agle se chota hai, toh decreasing nahi ho sakta
            if nums[i] < nums[i + 1]:
                is_decreasing = False
                
        # Agar dono mein se koi ek bhi True hai, toh return True
        return is_increasing or is_decreasing