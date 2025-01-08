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
        # self.cells : list[list[bool]] = [[False for _ in range(self.columns)] for _ in range(self.rows)]
        self.random_start_state()

    def random_start_state(self) -> None:
        """
        Randomly initializes the grid.
        """
        import random
        self.cells : list[list[bool]] = [[random.choice([True, False]) for _ in range(self.columns)] for _ in range(self.rows)]
    
    def draw(self, window : pygame.Surface) -> None:
        """
        Draws the grids on the window with the specified cell width.

        Args:
            window: The pygame window.
        """
        for row in range(self.rows):
            for column in range(self.columns):
                color = (0, 255, 0) if self.cells[row][column] else (0, 0, 0)
                pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))

    def count_neighbours(self, row : int, column : int) -> int:
        """
        Counts the number of neighbours of a cell.

        Args:
            row: The row of the cell.
            column: The column of the cell.

        Returns:
            The number of neighbours of the cell.
        """
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        neighbours_count = 0

        for nr, nc in neighbours:
            r = (row + nr) % self.rows
            c = (column + nc) % self.columns

            if self.cells[r][c]:
                neighbours_count += self.cells[r][c]
        
        return neighbours_count
    
    def update(self) -> None:
        """
        Updates the grid based on the rules of the game.
        """
        temp_cells : list[list[bool]] = [[False for _ in range(self.columns)] for _ in range(self.rows)]

        for row in range(self.rows):
            for column in range(self.columns):
                neighbours = self.count_neighbours(row, column)

                if self.cells[row][column]:
                    if neighbours < 2 or neighbours > 3:
                        temp_cells[row][column] = False
                    else:
                        temp_cells[row][column] = True
                else:
                    if neighbours == 3:
                        temp_cells[row][column] = True

        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = temp_cells[row][column]
