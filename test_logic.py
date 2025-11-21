import unittest
import numpy as np
from Grid import Grid

class TestGameOfLife(unittest.TestCase):
    def test_blinker(self):
        # Create a small grid
        grid = Grid(50, 50, 10) # 5x5 grid effectively
        # Reset cells to all False
        grid.cells[:] = False
        
        # Set up a blinker
        # Vertical line of 3
        grid.cells[1, 2] = True
        grid.cells[2, 2] = True
        grid.cells[3, 2] = True
        
        # Update
        grid.update()
        
        # Check if it became a horizontal line
        self.assertFalse(grid.cells[1, 2])
        self.assertFalse(grid.cells[3, 2])
        self.assertTrue(grid.cells[2, 1])
        self.assertTrue(grid.cells[2, 2])
        self.assertTrue(grid.cells[2, 3])
        
        # Update again
        grid.update()
        
        # Check if it became vertical again
        self.assertTrue(grid.cells[1, 2])
        self.assertTrue(grid.cells[2, 2])
        self.assertTrue(grid.cells[3, 2])
        self.assertFalse(grid.cells[2, 1])
        self.assertFalse(grid.cells[2, 3])

    def test_glider(self):
        # Glider pattern
        grid = Grid(100, 100, 10)
        grid.cells[:] = False
        
        # Glider at top left
        # 0 1 0
        # 0 0 1
        # 1 1 1
        grid.cells[0, 1] = True
        grid.cells[1, 2] = True
        grid.cells[2, 0] = True
        grid.cells[2, 1] = True
        grid.cells[2, 2] = True
        
        initial_sum = np.sum(grid.cells)
        
        # Run a few generations
        for _ in range(4):
            grid.update()
            
        # Glider should have moved but still have same number of cells (5)
        # Note: Glider period is 4, it moves diagonally.
        self.assertEqual(np.sum(grid.cells), initial_sum)
        
        # Check new position (shifted by 1, 1)
        self.assertTrue(grid.cells[1, 2])
        self.assertTrue(grid.cells[2, 3])
        self.assertTrue(grid.cells[3, 1])
        self.assertTrue(grid.cells[3, 2])
        self.assertTrue(grid.cells[3, 3])

if __name__ == '__main__':
    unittest.main()
