class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7
        n = len(board)
       
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        dp[n-1][n-1] = [0, 1]
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
          
                if board[r][c] == 'X' or (r == n - 1 and c == n - 1):
                    continue
                
                max_score = -1
                num_paths = 0
                
            
                directions = [(r + 1, c), (r, c + 1), (r + 1, c + 1)]
                
                for nr, nc in directions:
                    if nr < n and nc < n and dp[nr][nc][0] != -1:
                        next_score, next_paths = dp[nr][nc]
                        
                        if next_score > max_score:
                            max_score = next_score
                            num_paths = next_paths
                        elif next_score == max_score:
                            num_paths = (num_paths + next_paths) % MOD
                
                
                if max_score != -1:
                    # Calculate current cell 
                    cell_val = 0
                    if board[r][c].isdigit():
                        cell_val = int(board[r][c])
                    
                    dp[r][c] = [max_score + cell_val, num_paths]
    
        final_score, final_paths = dp[0][0]
        
        return [final_score if final_score != -1 else 0, final_paths]
