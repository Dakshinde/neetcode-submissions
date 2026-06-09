class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # print(board) # so its a [["","".......]]

        rows = {k: set() for k in range(9)}
        columns = {k: set() for k in range(9)}
        box = {(k,l): set() for k in range(3) for l in range(3)}

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell not in rows[i] and cell not in columns[j] and cell not in box[(i//3,j//3)]:
                    rows[i].add(cell)
                    columns[j].add(cell)
                    box[(i//3),(j//3)].add(cell)
                else:
                    return False
        
        return True

                