"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        m = matrix
        for b in range((n + 1) // 2):
            for a in range(n - 2 * b):
                print(b, a)
                m[b][b + a], m[b + a][n - b], m[n - b][n - b - a], m[n - b - a][b] = m[n - b - a][b], m[b][b + a], \
                                                                                     m[b + a][n - b], m[n - b][
                                                                                         n - b - a]
