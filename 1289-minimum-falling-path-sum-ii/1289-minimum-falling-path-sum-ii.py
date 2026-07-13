class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
            
        # Helper function jo kisi bhi row ke top 2 minimum values aur pehle waale ka index nikalta hai
        def get_two_mins(row):
            first_min, second_min = float('inf'), float('inf')
            first_min_idx = -1
            
            for c, val in enumerate(row):
                if val < first_min:
                    second_min = first_min
                    first_min = val
                    first_min_idx = c
                elif val < second_min:
                    second_min = val
            return first_min, first_min_idx, second_min

        # Pehli row ke liye top 2 minimums nikaalo
        prev_min1, prev_min1_idx, prev_min2 = get_two_mins(grid[0])
        
        # 1st row se lekar end tak loop chalao
        for r in range(1, n):
            current_row_sums = []
            
            for c in range(n):
                # Agar pichli row ka absolute minimum ka column index current column se alag hai
                if c != prev_min1_idx:
                    current_sum = grid[r][c] + prev_min1
                else:
                    # Agar index same ho gaya, toh second minimum choice lo
                    current_sum = grid[r][c] + prev_min2
                    
                current_row_sums.append(current_sum)
                
            # Agli row ke liye current row ke minimums ko 'previous' bana do
            prev_min1, prev_min1_idx, prev_min2 = get_two_mins(current_row_sums)
            
        # Aakhri row ka jo sabse chota sum hoga, wahi hamara answer hai
        return prev_min1