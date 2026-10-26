from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = defaultdict(int)
        count = 0
        
        # 1. Store all pairwise sums of nums1 and nums2 in Hash Map
        for u in nums1:
            for v in nums2:
                sum_map[u + v] += 1
                
        # 2. Check for negative of pairwise sums of nums3 and nums4
        for w in nums3:
            for x in nums4:
                target = -(w + x)
                if target in sum_map:
                    count += sum_map[target]
                    
        return count