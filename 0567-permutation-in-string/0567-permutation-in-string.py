class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        # Edge Case: Agar s1 bada hai s2 se
        if n1 > n2:
            return False
            
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # 1. Pehli window initialize karo
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        if s1_count == s2_count:
            return True
            
        # 2. Window ko right slide karo
        for i in range(n1, n2):
            # Naya character add karo (Window expansion)
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Purana character hatao (Window contraction)
            s2_count[ord(s2[i - n1]) - ord('a')] -= 1
            
            # Check if current window matches s1
            if s1_count == s2_count:
                return True
                
        return False