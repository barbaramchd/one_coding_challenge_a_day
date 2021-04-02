"""
1266. Minimum Time Visiting All Points
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

"""
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        output = 0  # sum of the seconds
        for pair in range(len(points) - 1):  # for each pair of coordinates
            diff = []  # store the difference of Xs and Ys for each two pairs of coordinates
            x_diff = points[pair][0] - points[pair + 1][0]  # difference between Xs
            diff.append(abs(x_diff))
            y_diff = points[pair][1] - points[pair + 1][1]  # difference between Ys
            diff.append(abs(y_diff))  # we only want the largest difference
            output += max(diff)

        return output
