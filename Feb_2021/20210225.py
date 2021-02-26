"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_number = 0
        for number in range(1, len(nums) + 1):
            if number not in nums:
                missing_number = number

        return missing_number