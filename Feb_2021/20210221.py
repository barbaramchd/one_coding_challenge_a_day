"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_sum = 0
        position = []

        while result_sum < target:

            for n in range(len(nums)):
                result_sum += nums[n]
                position.append(n)

                if result_sum == target:
                    break

        return position[-2:]