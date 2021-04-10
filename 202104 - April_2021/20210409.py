"""
  Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
"""
class Solution:
    def word_comp(self, string1, string2, order):
        if string1 == "":
            return True
        elif string2 == "":
            return False
        else:
            alien_order_string1 = order.index(string1[0])
            alien_order_string2 = order.index(string2[0])
            if alien_order_string1 < alien_order_string2:
                return True
            elif alien_order_string1 == alien_order_string2:
                string1_new = string1[1:]
                string2_new = string2[1:]
                return self.word_comp(string1_new, string2_new, order)
            else:
                return False

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        else:
            for index in range(len(words) - 1):
                result = self.word_comp(words[index], words[index + 1], order)

                if result == False:
                    return False

            return True


