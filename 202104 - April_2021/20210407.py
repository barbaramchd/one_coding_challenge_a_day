"""
Determine if String Halves Are Alike

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        a = s[:half]
        b = s[half:]
        vogels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a_vogels_counter = 0
        b_vogels_counter = 0
        for letter in range(half):
            if a[letter] in vogels_list:
                a_vogels_counter += 1

            if b[letter] in vogels_list:
                b_vogels_counter += 1

        if a_vogels_counter == b_vogels_counter:
            return True
        else:
            return False