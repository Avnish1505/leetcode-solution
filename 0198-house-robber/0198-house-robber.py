class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 represent karta hai ghar (i-2) tak ka max total
        # rob2 represent karta hai ghar (i-1) tak ka max total
        rob1, rob2 = 0, 0
        
        # Har ghar par jao aur faisla karo
        for n in nums:
            # Agar current ghar ko rob kiya toh: n + rob1
            # Agar skip kiya toh: rob2
            temp = max(n + rob1, rob2)
            
            # Agle ghar ke liye pointers ko aage shift karo
            rob1 = rob2
            rob2 = temp
            
        # Aakhir mein rob2 mein hamara final maximum answer hoga
        return rob2
        