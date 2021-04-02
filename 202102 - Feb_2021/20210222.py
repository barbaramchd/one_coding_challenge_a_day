"""
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list_of_indexes = []  # list of indexes of all the zeros in nums
        popped = []  # list of popped zeros

        # for loop to populate the list of indexes of zeros
        for element in range(len(nums)):
            if nums[element] == 0:
                list_of_indexes.append(element)

        for i in list_of_indexes:
            nums.pop(i - len(popped))
            popped.append(0)
            nums.append(0)

        return nums