# 0x07. Rotate 2D Matrix

## Task
The task is to rotate an `n x n` 2D matrix 90 degrees clockwise in place.

## Requirements
- The matrix will have exactly 2 dimensions (i.e., a 2D list).
- The function should modify the matrix in place without returning anything.
- The solution should use in-place operations to minimize space complexity.

## Solution
We solve this problem using two main steps:
1. **Transpose** the matrix: Swap the elements at positions `(i, j)` and `(j, i)` for all `i < j`.
2. **Reverse** each row to get the matrix rotated by 90 degrees clockwise.

### Example:
Given the matrix:

