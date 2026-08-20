class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_remain = Counter()
        guess_remain = Counter()
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_remain[s] += 1
                guess_remain[g] += 1
                
        # Common digits across non-bull characters
        cows = 0
        for digit in guess_remain:
            if digit in secret_remain:
                cows += min(secret_remain[digit], guess_remain[digit])
                
        return f"{bulls}A{cows}B"