"""
Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        global matrix2
        matrix2 = matrix
        m = len(matrix)
        n = len(matrix[0])

        max_path = -1
        for y in range(m):
            for x in range(n):
                new_path = self.path_calculator(x, y, m, n)
                if new_path > max_path:
                    max_path = new_path

        return max_path

    @lru_cache(maxsize=200 * 200)
    def path_calculator(self, x, y, m, n):
        global matrix2
        matrix = matrix2
        # top
        top = 0
        if 0 <= y - 1:
            if matrix[y][x] < matrix[y - 1][x]:
                top = self.path_calculator(x, y - 1, m, n)

        # bottom
        bottom = 0
        if y < (m - 1):
            if matrix[y][x] < matrix[y + 1][x]:
                bottom = self.path_calculator(x, y + 1, m, n)

        # left
        left = 0
        if 0 <= x - 1:
            if matrix[y][x] < matrix[y][x - 1]:
                left = self.path_calculator(x - 1, y, m, n)

        # right
        right = 0
        if x < (n - 1):
            if matrix[y][x] < matrix[y][x + 1]:
                right = self.path_calculator(x + 1, y, m, n)

        return max(top, bottom, left, right) + 1