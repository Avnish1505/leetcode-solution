class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        # Agar koi operation nahi hai, toh poora matrix hi max integers (0s) se bhara hai
        if not ops:
            return m * n
            
        min_row = m
        min_col = n
        
        # Sabhi operations ka minimum intersection region nikaalo
        for a, b in ops:
            min_row = min(min_row, a)
            min_col = min(min_col, b)
            
        return min_row * min_col