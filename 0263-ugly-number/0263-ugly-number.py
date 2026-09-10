class Solution:
    def isUgly(self, n: int) -> bool:
      # Non-positive numbers ugly nahi hote
        if n <= 0:
            return False
            
        # 2, 3, aur 5 se repeatedly divide karo
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
                
        # Agar sirf 2, 3, 5 hi factors the, toh n reduction ke baad 1 ban jayega
        return n == 1  