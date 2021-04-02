"""
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

#SOLUTION 1: USING FUNCTOOLS

from functools import lru_cache

class Solution:
    @lru_cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif n > 2:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)


# SOLUTION 2

class Solution:
    def __init__(self):
        self.dict_cache = {}

    def tribonacci(self, n: int) -> int:
        if n in self.dict_cache:
            return self.dict_cache[n]

        tn = 0
        if n == 0:
            tn = 0
        elif n == 1 or n == 2:
            tn = 1
        elif n > 2:
            tn = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        self.dict_cache[n] = tn

        return self.dict_cache[n]