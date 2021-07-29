"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_nums = {}

        # looping through the nums and creating a dict with
        # num as dict key and the num's count as the value
        for num in range(len(nums)):
            if nums[num] not in dict_nums:
                dict_nums[nums[num]] = 1
            else:
                dict_nums[nums[num]] += 1

        # looping through the dict and getting the keys with value == 1
        # return first key
        keys = [k for k, value in dict_nums.items() if value == 1]
        if keys:
            return keys[0]
        return None