from functools import cache
from collections import Counter

class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        # Base Case 1: Strings match exactly
        if s1 == s2:
            return True
            
        # Base Case 2: Character counts don't match (Pruning)
        if Counter(s1) != Counter(s2):
            return False
            
        n = len(s1)
        
        # Har possible split point check karo
        for i in range(1, n):
            # Case 1: No swap
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
                
            # Case 2: Swapped
            if self.isScramble(s1[:i], s2[n - i:]) and self.isScramble(s1[i:], s2[:n - i]):
                return True
                
        return False