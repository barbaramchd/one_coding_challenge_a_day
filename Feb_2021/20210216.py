"""
119. Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # previous row starts with row index 1, so it has element 1
        previous_row = [1]

        # empty list to store elements of current row
        current_row = []

        # edge case
        if rowIndex == 0:
            return previous_row

        # for each row, append one as the first element of each row
        # range() is not inclusive so range(rowIndex+1)
        for index in range(rowIndex + 1):
            current_row.append(1)

            # if index of the row is larger than 1
            # iterate through the elements in the row (minus the last element)
            if index > 1:
                for element_position in range(index - 1):
                    # the elements that are not in the extremes of the row, will be equal
                    # to the element in the same position in the previous row
                    # plus the element in the next position in the previous row
                    current_row.append(previous_row[element_position]
                                       + previous_row[element_position + 1])

            # append 1 as last element in each row
            current_row.append(1)
            # set previous row to be equal to current row
            previous_row = current_row
            # empty the current row
            current_row = []
        return previous_row