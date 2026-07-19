class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        
        # Effective shifts calculate karo (agar k > total ho)
        k = k % total
        
        # Naya empty grid initialize karo
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # 1. Purani 2D index ko 1D mein badlo
                old_1d = r * n + c
                
                # 2. Nayi 1D index nikalo k steps aage badha kar
                new_1d = (old_1d + k) % total
                
                # 3. Nayi 1D index ko wapas 2D coordinates mein convert karo
                new_r = new_1d // n
                new_c = new_1d % n
                
                # Value place kar do
                result[new_r][new_c] = grid[r][c]
                
        return result