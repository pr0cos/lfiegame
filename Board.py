import Cell


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.top = 10
        self.left = 10
        self.cell_size = 30
        self.board = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append(Cell.Cell(x, y))
            self.board.append(row)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j].render(screen, self.left, self.top, self.cell_size)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        x0 = x // self.cell_size
        y0 = y // self.cell_size
        if x0 < 0 or x0 >= self.width or y0 < 0 or y0 >= self.height:
            return None
        return x0, y0

    def on_click(self, cell):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
