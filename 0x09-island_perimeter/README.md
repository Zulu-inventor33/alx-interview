# 0x09. Island Perimeter

## Description
This project involves solving a problem of calculating the perimeter of an island in a 2D grid. The grid contains values of `1` representing land and `0` representing water. The goal is to calculate the perimeter of the land island using the given grid.

### Function
- **`island_perimeter(grid)`**: 
  - **Input**: A 2D list representing the grid where `1` represents land and `0` represents water.
  - **Output**: An integer representing the perimeter of the island.
  
### Problem Constraints
- The grid is rectangular with dimensions not exceeding 100x100.
- The grid is surrounded by water, and there is only one island.
- The island has no "lakes" (water regions within the land).

### Algorithm
The algorithm loops through the grid, checking for land cells (`1`). For each land cell, we check its four possible neighboring cells (up, down, left, right). If the neighboring cell is either out of bounds or water (`0`), we add to the perimeter count.

### Example
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12

