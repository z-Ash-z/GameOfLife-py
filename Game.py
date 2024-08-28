import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import sys
import pygame

from Simulation import Simulation


def main() -> None:
    pygame.init()

    FPS = 30
    CELL_SIZE = 25
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 1000
    GREY = (100, 100, 100)

    pygame.display.set_caption("Game of Life")

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
    simulation.grid.cells[3][4] = 1

    # Simulation Loop
    while True:

        # 1. Event Handling
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 2. Updating the State

        # 3. Drawing
        window.fill(GREY)
        simulation.draw(window)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()