# import os
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import sys
import pygame

from Simulation import Simulation


def main() -> None:
    pygame.init()

    # Initializing the default values.
    FPS = 30

    CELL_SIZE = 5
    WINDOW_WIDTH = 2000
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

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RIGHT:
                    FPS = min(60, FPS + 2)
                elif event.key == pygame.K_LEFT:
                    FPS = max(1, FPS - 2)
                elif event.key == pygame.K_SPACE:
                    simulation.toggle_pause(window)
                elif event.key == pygame.K_c:
                    simulation.clear()
                elif event.key == pygame.K_r:
                    simulation.random_start_state()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // CELL_SIZE
                column = pos[0] // CELL_SIZE
                simulation.toggle_cell(row, column)

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