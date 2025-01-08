import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import sys
import pygame

from Simulation import Simulation


def main() -> None:
    pygame.init()

    # Initializing the default values.
    FPS = 30

    CELL_SIZE = 5
    WINDOW_WIDTH = 1500
    WINDOW_HEIGHT = 1000
    GREY = (100, 100, 100)

    pygame.display.set_caption("Game of Life")

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

    # Simulation Loop
    running = True
    while running:

        # 1. Event Handling
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False

        # 2. Updating the State
        simulation.update()

        # 3. Drawing
        window.fill(GREY)
        simulation.draw(window)

        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()