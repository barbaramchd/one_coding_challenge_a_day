"""
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest_substring = ""
        opening_parenthesis = 0
        closing_parenthesis = 0
        start_point = 0

        for p in range(len(s)):
            if s[p] == "(":
                opening_parenthesis += 1
            else:
                closing_parenthesis += 1

            if opening_parenthesis < closing_parenthesis:

                if len(longest_substring) < len(s[start_point:p]):
                    print(1)
                    longest_substring = s[start_point:p]

                start_point = p + 1
                opening_parenthesis = 0
                closing_parenthesis = 0

        if opening_parenthesis == closing_parenthesis:

            if len(longest_substring) < len(s[start_point:]):
                print(2)
                longest_substring = s[start_point:]

        if opening_parenthesis > closing_parenthesis:
            # longest_substring = ""
            opening_parenthesis = 0
            closing_parenthesis = 0
            start_point = len(s) - 1
            for p in range(len(s) - 1, -1, -1):
                if s[p] == "(":
                    opening_parenthesis += 1
                else:
                    closing_parenthesis += 1
                if opening_parenthesis > closing_parenthesis:
                    if len(longest_substring) < len(s[p:start_point]):
                        print(3)
                        longest_substring = s[p:start_point]

                    start_point = p - 1
                    opening_parenthesis = 0
                    closing_parenthesis = 0

                if opening_parenthesis == closing_parenthesis:

                    if len(longest_substring) < len(s[p:start_point + 1]):
                        print(4)
                        longest_substring = s[p:start_point + 1]

        print(longest_substring)
        return len(longest_substring)
