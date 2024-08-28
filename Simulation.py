import pygame
from Grid import Grid

class Simulation:

    def __init__(self, width : int, height : int, cell_size : int) -> None:
        self.grid = Grid(width, height, cell_size)

    def draw(self, window : pygame.display.__spec__) -> None:
        self.grid.draw(window)