"""
  Range Addition

You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.
"""

import numpy as np


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        old_output = [0] * length
        output = np.array(old_output)

        for update in updates:
            output[update[0]:update[1] + 1] = output[update[0]:update[1] + 1] + update[2]

        return output