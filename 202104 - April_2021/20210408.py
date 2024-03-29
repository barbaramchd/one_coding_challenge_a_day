"""
Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter_dict = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        combinations = []
        for index in range(len(digits)):
            combinations2 = []
            if len(combinations) == 0:
                combinations = list(digit_to_letter_dict[digits[index]])
            else:
                for value1 in range(len(combinations)):
                    for value2 in digit_to_letter_dict[digits[index]]:
                        comb = combinations[value1] + value2
                        combinations2.append(comb)
                combinations = combinations2

        return combinations