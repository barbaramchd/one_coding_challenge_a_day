"""
  Largest Unique Number

Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.
"""
import numpy as np

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        A_new = np.sort(A)
        reverse_A = A_new[::-1]
        if len(A) == 1:
            return A[0]
        else:
            numbers_dict = {}
            for number in range(len(reverse_A)):
                if reverse_A[number] not in numbers_dict:
                    numbers_dict[reverse_A[number]] = 1
                else:
                    numbers_dict[reverse_A[number]] += 1

            for key in numbers_dict:
                if numbers_dict[key] == 1:
                    return key

            return -1