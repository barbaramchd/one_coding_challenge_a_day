"""
383. Ransom Note

Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        dict_letters = {}
        for c in magazine:
            if c in dict_letters:
                dict_letters[c] += 1
            else:
                dict_letters[c] = 1

        for j in ransomNote:
            if j not in dict_letters:
                return False
            if dict_letters[j] < 1:
                return False

            dict_letters[j] -= 1

        return True