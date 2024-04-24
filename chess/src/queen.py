from src.piece import Piece


class Queen(Piece):
    def char(self):
        return 'Q'
    
    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        diff_row = abs(row - row_1)
        diff_col = abs(col - col_1)
        if diff_row == 0 and diff_col != 0:
            return self.check_horizontal(board, row, col, row_1, col_1)
        elif diff_col == 0 and diff_row != 0:
            return self.check_vertical(board, row, col, row_1, col_1)
        elif diff_row == diff_col:
            return self.check_diagonal(board, row, col, row_1, col_1)
        return False
    
    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)
