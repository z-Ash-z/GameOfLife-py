import pygame

class Grid:
    """
    Class to draw and maintain the grid window.
    """
    def __init__(self, width : int, height : int, cell_size : int) -> None:
        """
        Class to draw and maintain the grid window.

        Args:
            width: The width of the window.
            height: The height of the window.
            cell_size: The size of each cell in the window.
        """
        self.rows : int= height // cell_size
        self.columns : int = width // cell_size
        self.cell_size : int = cell_size
        self.cells : list[list[bool]]= [[False for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window : pygame.display.__spec__) -> None:
        """
        Draws the grids on the window with the specified cell width.

        Args:
            window: The pygame window.
        """
        for row in range(self.rows):
            for column in range(self.columns):
                color = (0, 255, 0) if self.cells[row][column] else (0, 0, 0)
                pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))
