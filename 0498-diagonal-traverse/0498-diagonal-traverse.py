class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
            
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        # Step 1: Saare elements ko unke (r + c) sum ke hisab se group karo
        for r in range(m):
            for c in range(n):
                diagonals[r + c].append(mat[r][c])
                
        result = []
        
        # Step 2: Total diagonals honge (m + n - 1)
        for sum_key in range(m + n - 1):
            if sum_key % 2 == 0:
                # Even sum: Bottom-Up movement ke liye reverse karke add karo
                result.extend(diagonals[sum_key][::-1])
            else:
                # Odd sum: Top-Down movement ke liye directly add karo
                result.extend(diagonals[sum_key])
                
        return result