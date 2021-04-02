"""
58. Length of Last Word
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_new = s.rstrip()
        last_word = []
        for letter in range(1, len(s_new) + 1):
            if s_new[-letter] == " ":
                break
            else:
                last_word.append(s_new[-letter])

        return len(last_word)