class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # 1. Board par Rook ('R') ki position find karo
        rook_r, rook_c = 0, 0
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    rook_r, rook_c = r, c
                    break
                    
        captures = 0
        # 4 directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # 2. Har direction mein seedha aage badho
        for dr, dc in directions:
            curr_r, curr_c = rook_r + dr, rook_c + dc
            
            while 0 <= curr_r < 8 and 0 <= curr_c < 8:
                # Agar White Bishop ('B') mila toh path block ho gaya
                if board[curr_r][curr_c] == 'B':
                    break
                # Agar Black Pawn ('p') mila toh capture count badhao aur ruk jao
                if board[curr_r][curr_c] == 'p':
                    captures += 1
                    break
                    
                # Khali square ('.') hai toh usi direction mein ek step aur aage badho
                curr_r += dr
                curr_c += dc
                
        return captures