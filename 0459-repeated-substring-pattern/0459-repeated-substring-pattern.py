class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        # Pattern ki length max n // 2 ho sakti hai
        for l in range(1, n // 2 + 1):
            if n % l == 0:
                substring = s[:l]
                # Check karo kya substring ko repeat karke original s ban raha hai
                if substring * (n // l) == s:
                    return True
                    
        return False