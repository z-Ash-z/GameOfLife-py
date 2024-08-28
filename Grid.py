import pygame

class Grid:

    def __init__(self, width : int, height : int, cell_size : int) -> None:
        
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window : pygame.display.__spec__) -> None:

        for row in range(self.rows):
            for column in range(self.columns):
                color = (0, 255, 0) if self.cells[row][column] else (0, 0, 0)
                pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))
