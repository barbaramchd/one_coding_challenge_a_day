"""
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""
# SOLUTION 1
class Solution:
    def fib(self, n: int) -> int:
        if n > 1:
            return self.fib(n - 1) + self.fib(n - 2)
        elif n == 1:
            return 1
        else:
            return 0


# SOLUTION 2: WITH MEMOIZATION
dict_cache = {}
class Solution:
    def fib(self, n: int) -> int:
        if n in dict_cache:
            return dict_cache[n]
        if n > 1:
            dict_cache[n] = self.fib(n-1) + self.fib(n-2)
            return dict_cache[n]
        if n == 1:
            return 1
        else:
            return 0