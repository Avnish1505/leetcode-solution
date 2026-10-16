from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = defaultdict(int)
        
        # 1. Standardize karke count store karo
        for a, b in dominoes:
            # Hamesha chota number pehle, bada baad mein
            key = (min(a, b), max(a, b))
            counts[key] += 1
            
        total_pairs = 0
        
        # 2. Har unique domino ke pairs calculate karo: n * (n - 1) // 2
        for count in counts.values():
            if count > 1:
                total_pairs += (count * (count - 1)) // 2
                
        return total_pairs