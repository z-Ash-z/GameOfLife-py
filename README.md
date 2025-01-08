# Conway's Game of life

## What does this project do?

This project simulates Conway's Game of Life, a cellular automaton devised by mathematician John Conway. It demonstrates how complex patterns and behaviors can emerge from simple rules applied to a grid of cells over successive generations.

Conway's algorithm tried to simulate three scenarios for life: Underpopulation, Stasis and Overpopulation. 

- Underpopulation - A live cell with fewer than two live neighbours.
- Statis - A live cell with two or three neighbours lives onto the next generation.
- Overpopulaiton  - A live cell with more than three live neighbours dies.

The rules for the game can be broken down into:
1. Any live cell with fewer than two live neighbours dies.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies.
4. Any dead cell with exactly three live neighbours becomes a live cell.