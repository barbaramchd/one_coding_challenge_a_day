"""
1351. Count Negative Numbers in a Sorted Matrix
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for m in range(len(grid)):
            for r in range(len(grid[m])):
                if grid[m][r] < 0:
                    neg += 1
        return neg