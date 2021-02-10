"""
1684. Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consist_count = 0
        for s in range(len(words)):
            for c in range(len(words[s])):
                # if the character in word[s] is in the allowed
                if (words[s][c] in allowed):

                    if c == (len(words[s]) - 1):
                        consist_count += 1
                else:
                    # if one letter in the word is not in the string
                    # break and iterate through the next word
                    break
        return consist_count