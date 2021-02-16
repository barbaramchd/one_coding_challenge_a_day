"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = []  # store current substring

        # store the length of longest substring
        length_of_max_substring = 0

        # if empty string, return 0
        if len(s) == 0:
            return 0

        # for each character in the string, I will check
        # if it is already in the current substring
        for character in range(len(s)):
            if s[character] in current_substring:
                # getting the index of the duplicated character in the current substring
                index = current_substring.index(s[character])

                # as it is duplicated, we need to delete the current substring
                # up to the duplicated character
                # we need to delete everything because sometimes it
                # duplicates with some "spacement"/ not consecutives characters
                del current_substring[:index + 1]

                # append the current character to the new created current substring
                current_substring.append(s[character])

                # if the character is not in the current substring, I will append it
            else:
                current_substring.append(s[character])

                # if the length of the current substring is larger
                # than length_of_max_substring, update length_of_max_substring
                if length_of_max_substring < len(current_substring):
                    length_of_max_substring = len(current_substring)

        return length_of_max_substring