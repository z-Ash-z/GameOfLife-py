import pygame
from Grid import Grid

class Simulation:
    """
    Class to handle the simulation on pygame.
    """
    def __init__(self, width : int, height : int, cell_size : int) -> None:
        self.grid = Grid(width, height, cell_size)

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
        self.grid.update()