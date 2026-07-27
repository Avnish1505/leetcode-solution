class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = -1
        
        while n > 0:
            current_bit = n % 2  # ya n & 1
            if current_bit == prev_bit:
                return False
            prev_bit = current_bit
            n //= 2              # ya n >>= 1
            
        return True