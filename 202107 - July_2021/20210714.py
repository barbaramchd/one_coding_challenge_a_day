"""
  Custom Sort String

order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.
"""


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        index_replaced = []
        index_notreplaced = []

        for c in range(len(str)):
            if str[c] in order:
                index_replaced.append(c)
            else:
                index_notreplaced.append(c)

        characters_replaced = ""
        not_replaced = ""
        for i in index_replaced:
            characters_replaced += str[i]

        for i in index_notreplaced:
            not_replaced += str[i]

        return order + not_replaced