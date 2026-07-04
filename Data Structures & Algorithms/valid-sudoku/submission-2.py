from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]

        grid = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                val = board[i][j]
                grid_key = (i // 3, j // 3)

                if val in rows[i] or val in cols[j]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                
                if val in grid[grid_key]:
                    return False

                grid[grid_key].add(val)
    
        return True
