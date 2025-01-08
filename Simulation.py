import pygame
from Grid import Grid

class Simulation:
    """
    Class to handle the simulation on pygame.
    """
    def __init__(self, width : int, height : int, cell_size : int) -> None:
        self.grid = Grid(width, height, cell_size)
        self.pause = True

    def draw(self, window : pygame.Surface) -> None:
        """
        Draws the grid on the window.

        Args:
            window: The pygame window.
        """
        self.grid.draw(window)

    def update(self) -> None:
        """
        Updates the grid based on the rules of the game.
        """
        if not self.pause:
            self.grid.update()

    def toggle_pause(self, window : pygame.Surface) -> None:
        """
        Toggles the pause state of the simulation.
        """
        self.pause = not self.pause
        if self.pause:
            pygame.display.set_caption("Game of Life - Paused")
        else:
            pygame.display.set_caption("Game of Life - Running")

    def toggle_cell(self, row : int, column : int) -> None:
        """
        Toggles the state of a cell.

        Args:
            row: The row of the cell.
            column: The column of the cell.
        """
        if self.pause:
            self.grid.cells[row][column] = not self.grid.cells[row][column]

    def clear(self) -> None:
        """
        Clears the grid.
        """
        if self.pause:
            self.grid.clear()

    def random_start_state(self) -> None:
        """
        Randomly initializes the grid.
        """
        if self.pause:
            self.grid.random_start_state()