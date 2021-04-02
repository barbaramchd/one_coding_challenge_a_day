"""
1232. Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        output = True
        # calculate the different between first and second Ys
        y_diff = coordinates[1][1] - coordinates[0][1]
        # calculate the different between first and second Xs
        x_diff = coordinates[1][0] - coordinates[0][0]

        # when the Xs difference is zero
        # it should not change
        if x_diff == 0:
            for pair in range(len(coordinates)):
                if coordinates[pair][0] != coordinates[pair - 1][0]:
                    return False
        else:
            # using the linear equation y = m*x + b
            m = y_diff / x_diff
            b = coordinates[0][1] - m * coordinates[0][0]
            for pair in range(len(coordinates)):
                y_coordinate = m * coordinates[pair][0] + b
                if y_coordinate != coordinates[pair][1]:
                    return False
        return output

