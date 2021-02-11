"""
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter_list = []
        for i in range(len(nums)):
            counter = 0  # we have a counter for each number i
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter += 1

            counter_list.append(counter)
        return counter_list