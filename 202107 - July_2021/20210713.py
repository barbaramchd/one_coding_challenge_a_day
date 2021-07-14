"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = 0
        nums.append(float('-inf'))
        for index in range(len(nums)-1):
            if nums[index] > nums[index-1]:
                if nums[index] > nums[index+1]:
                    peak = index
                    break
        return peak