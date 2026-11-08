from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 1. Magazine ke characters ki frequency count karo
        counts = Counter(magazine)
        
        # 2. RansomNote ke har character ko check karo
        for char in ransomNote:
            # Agar character khatam ho gaya ya hai hi nahi
            if counts[char] <= 0:
                return False
            # Character count ghata do
            counts[char] -= 1
            
        return True