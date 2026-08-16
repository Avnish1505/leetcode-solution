import re
import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Regex se saare numerators aur denominators extract karo
        # Example "-1/2+1/3" -> [('-1', '2'), ('+1', '3')]
        fractions = re.findall(r'([+-]?\d+)/(\d+)', expression)
        
        num = 0
        den = 1
        
        for n, d in fractions:
            n = int(n)
            d = int(d)
            
            # Cross-multiplication formula se running sum update karo
            num = num * d + n * den
            den = den * d
            
        # Simplest form mein convert karne ke liye GCD se divide karo
        common = math.gcd(abs(num), den)
        num //= common
        den //= common
        
        return f"{num}/{den}"