import pygame
import numpy as np

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
        self.cells = np.zeros((self.rows, self.columns), dtype=bool)

    def clear(self) -> None:
        """
        Clears the grid.
        """
        self.cells = np.zeros((self.rows, self.columns), dtype=bool)

    def random_start_state(self) -> None:
        """
        Randomly initializes the grid.
        """
        self.cells = np.random.choice([True, False], size=(self.rows, self.columns), p=[0.1, 0.9])
    
    def draw(self, window : pygame.Surface) -> None:
        """
        Draws the grids on the window with the specified cell width.

        Args:
            window: The pygame window.
        """
        # Create an image from the grid
        # Alive cells are green (0, 255, 0), dead are black (0, 0, 0)
        # We need an array of shape (width, height, 3) for surfarray.blit_array
        # But self.cells is (rows, cols). We need to transpose to (cols, rows) -> (x, y)
        
        # Create a surface for the grid (1 pixel per cell)
        surface = pygame.Surface((self.columns, self.rows))
        
        # Create an RGB array
        # Initialize with black
        img_array = np.zeros((self.columns, self.rows, 3), dtype=np.uint8)
        
        # Set green channel where cells are alive
        # Transpose cells to match (x, y)
        cells_t = self.cells.T
        img_array[cells_t, 1] = 255 # Green channel
        
        pygame.surfarray.blit_array(surface, img_array)
        
        # Scale up to window size
        pygame.transform.scale(surface, window.get_size(), window)

    def update(self) -> None:
        """
        Updates the grid based on the rules of the game.
        """
        # Count neighbours using rolling
        # This wraps around the edges (toroidal grid)
        # We need to cast to int so that True + True = 2, not True (if it were boolean logic)
        cells_int = self.cells.astype(int)
        neighbours = (
            np.roll(cells_int, 1, axis=0) +  # Down
            np.roll(cells_int, -1, axis=0) + # Up
            np.roll(cells_int, 1, axis=1) +  # Right
            np.roll(cells_int, -1, axis=1) + # Left
            np.roll(np.roll(cells_int, 1, axis=0), 1, axis=1) +   # Down-Right
            np.roll(np.roll(cells_int, 1, axis=0), -1, axis=1) +  # Down-Left
            np.roll(np.roll(cells_int, -1, axis=0), 1, axis=1) +  # Up-Right
            np.roll(np.roll(cells_int, -1, axis=0), -1, axis=1)   # Up-Left
        )

        # Apply rules
        # 1. Any live cell with 2 or 3 live neighbours survives.
        # 2. Any dead cell with 3 live neighbours becomes a live cell.
        # 3. All other live cells die in the next generation.
        # 4. All other dead cells stay dead.
        
        # Rule 1 & 3: Live cells stay alive if neighbours is 2 or 3
        stay_alive = (self.cells) & ((neighbours == 2) | (neighbours == 3))
        
        # Rule 2: Dead cells become alive if neighbours is 3
        born = (~self.cells) & (neighbours == 3)
        
        # Update cells
        self.cells = stay_alive | born
