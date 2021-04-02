"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows > 1:
            previous_row = numRows - 1  # get the number of the last row
            list_of_previous_rows = self.generate(previous_row)
            current_row = []
            for i in range(numRows):
                if i == 0:
                    current_row.append(1)
                elif i == numRows - 1:
                    current_row.append(1)
                else:
                    # get the elements for the lists that are not in the extreme
                    middle_values = list_of_previous_rows[-1][i - 1] + list_of_previous_rows[-1][i]
                    current_row.append(middle_values)
            list_of_previous_rows.append(current_row)
            return list_of_previous_rows
