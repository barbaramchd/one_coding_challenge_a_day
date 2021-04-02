"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        counter = 0
        for element in range(len(s)):
            if s[element] == "M":
                counter += 1000
            elif s[element] == "D":
                counter += 500
            elif s[element] == "C":
                index = element + 1
                if index < len(s):
                    if s[index] == "M" or s[index] == "D":
                        counter -= 100
                    else:
                        counter += 100
                else:
                    counter += 100
            elif s[element] == "L":
                counter += 50
            elif s[element] == "X":
                index = element + 1
                if index < len(s):
                    if s[index] == "C" or s[index] == "L":
                        counter -= 10
                    else:
                        counter += 10
                else:
                    counter += 10
            elif s[element] == "V":
                counter += 5
            elif s[element] == "I":
                index = element + 1
                if index < len(s):
                    if s[index] == "X" or s[index] == "V":
                        counter -= 1
                    else:
                        counter += 1
                else:
                    counter += 1
        return counter
