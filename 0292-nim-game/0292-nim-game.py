class Solution:
    def canWinNim(self, n: int) -> bool:
        # Agar n 4 ka multiple nahi hai, toh hum jeet jayenge
        return n % 4 != 0