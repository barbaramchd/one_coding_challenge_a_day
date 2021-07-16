"""
  Valid Triangle Number

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.


"""

from itertools import combinations


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        combination = 0

        if len(nums) >= 3:

            comb = combinations(nums, 3)

            for sides in comb:
                large = max(sides)
                sides_copy = list(sides)
                sides_copy.remove(large)
                if sum(sides_copy) > large:
                    combination += 1

        return combination
