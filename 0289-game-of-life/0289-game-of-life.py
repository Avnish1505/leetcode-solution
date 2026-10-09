class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        # 8 directions for neighbors: (row_change, col_change)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        # Pass 1: Temporary state markers
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                
                # Check all 8 neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (1, 2):
                        live_neighbors += 1
                
                # Rule 1 & 3: Live cell dies -> Mark as 2
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2
                # Rule 4: Dead cell comes to life -> Mark as 3
                elif board[r][c] == 0:
                    if live_neighbors == 3:
                        board[r][c] = 3
                        
        # Pass 2: Convert intermediate states (2 -> 0, 3 -> 1)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1