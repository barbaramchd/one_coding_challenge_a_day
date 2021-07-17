"""
4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""
from itertools import combinations


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        combination = []

        if len(nums) >= 4:

            tupple = combinations(nums, 4)

            for comb in tupple:
                if sum(comb) == target:
                    comb_list = list(comb)
                    comb_list.sort()
                    if comb_list not in combination:
                        combination.append(comb_list)

        return combination