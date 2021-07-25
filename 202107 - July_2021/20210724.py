"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

# decreasing time limit for recursion
import sys

sys.setrecursionlimit(10 ** 2)


class Solution:
    def isHappy(self, n: int) -> bool:
        number = n
        # transforming the number in string
        # so I can loop through it
        number_str = str(number)

        calc = 0
        # if i dont have a number, return false
        if len(number_str) == 0: return False

        if len(number_str) >= 1:
            for digit in range(len(number_str)):
                # square every digit and add it to calc
                digit_int = int(number_str[digit])
                calc += digit_int ** 2

        # if the sum of squares equals one
        # we return true
        if calc == 1:
            return True

        # else, call calc recursively
        # and returns false if it loops endlessly
        # in a cycle which does not include 1.
        else:
            try:
                return self.isHappy(calc)
            except:
                return False