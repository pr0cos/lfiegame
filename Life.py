import Board
import Cell


class Life(Board.Board):
    def on_click(self, cell):
        x, y = cell
        self.board[x][y].state = not self.board[x][y].state

    def next_move(self):
        next_board = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append(Cell.Cell(x, y))
            next_board.append(row)
        for x in range(self.width):
            for y in range(self.height):
                cells = ((-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (0, 1), (1, 0))
                near_alive = 0
                for cell in cells:
                    try:
                        i = x + cell[0]
                        j = y + cell[1]
                        if i >= 0 and j >= 0:
                            if self.board[i][j].state:
                                near_alive += 1
                    except IndexError:
                        pass
                if near_alive == 2 or near_alive == 3:
                    next_board[x][y] = Cell.Cell(x, y, state=True)
                else:
                    next_board[x][y] = Cell.Cell(x, y)
        self.board = next_board.copy()
