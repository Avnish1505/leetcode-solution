class Solution:
    def findLHS(self, nums: list[int]) -> int:
        from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # 1. Array ke elements ki frequency count karo
        freq = Counter(nums)
        max_length = 0
        
        # 2. Har number x ke liye check karo ki kya x + 1 bhi hai
        for x in freq:
            if x + 1 in freq:
                # Harmonious subsequence ki length = count of x + count of (x + 1)
                current_length = freq[x] + freq[x + 1]
                max_length = max(max_length, current_length)
                
        return max_length