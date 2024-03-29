"""
1732. Find the Highest Altitude
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""

# SOLUTION 1
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        list_alt = [0]
        current_alt = 0
        for i in range(len(gain)):
            current_alt += gain[i]
            list_alt.append(current_alt)

        return max(list_alt)

# SOLUTION 2
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        list_alt = [0] # list to store altitudes
        for i in range(len(gain)):
            # adding the difference of altitudes to the previous altitude
            list_alt.append(gain[i] + list_alt[-1])

        return max(list_alt)