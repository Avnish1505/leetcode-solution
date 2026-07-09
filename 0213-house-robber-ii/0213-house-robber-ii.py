class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base Case: Agar sirf ek hi ghar hai, toh use hi loot lo
        if len(nums) == 1:
            return nums[0]
        
        # Purana House Robber 1 wala logic (Linear Array ke liye)
        def linear_rob(houses):
            rob1, rob2 = 0, 0
            for n in houses:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        # Option 1: Pehle ghar se aakhri se ek pehle tak -> nums[:-1]
        # Option 2: Doosre ghar se bilkul aakhri tak -> nums[1:]
        option1 = linear_rob(nums[:-1])
        option2 = linear_rob(nums[1:])
        
        # Dono mein se jo max profit dega, wahi hamara answer hai
        return max(option1, option2)
        