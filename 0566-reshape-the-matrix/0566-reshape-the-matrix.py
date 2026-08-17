class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # Condition check: Total elements match hone chahiye
        if m * n != r * c:
            return mat
            
        # Naya reshaped matrix initialize karo
        result = [[0] * c for _ in range(r)]
        
        # Sequential index mapping
        for k in range(m * n):
            # Original matrix coordinates
            old_r, old_c = k // n, k % n
            
            # New matrix coordinates
            new_r, new_c = k // c, k % c
            
            result[new_r][new_c] = mat[old_r][old_c]
            
        return result