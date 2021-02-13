"""
1614. Maximum Nesting Depth of the Parentheses

A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.
"""

# SOLUTION 1
class Solution:
    def maxDepth(self, s: str) -> int:
        depth_counter = []
        open_character = 0
        close_character = 0
        for character in range(len(s)):
            if s[character] == "(":
                open_character += 1
            if s[character] == ")":
                close_character += 1

            depth_counter.append(open_character - close_character)
        return max(depth_counter)

# SOLUTION 2 (with less memory bc I dont need to keep a list)
class Solution:
    def maxDepth(self, s: str) -> int:
        depth_counter = 0
        open_character = 0
        close_character = 0
        for character in range(len(s)):
            if s[character] == "(":
                open_character += 1
            if s[character] == ")":
                close_character += 1

            depth_counter_cal = open_character - close_character
            if depth_counter_cal > depth_counter:
                depth_counter = depth_counter_cal

        return depth_counter