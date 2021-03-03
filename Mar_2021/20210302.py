"""
917. Reverse Only Letters
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
"""
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # empty list to store the elements of the string in reverse order
        reversed_list = []

        # range needs to go form 1 to len+1 because we are going in reverse order
        # so we dont want to start from zero
        for character in range(1, len(S) + 1):
            # checking if character is alphabetic
            if S[-character].isalpha():
                # append the character in reverse order
                reversed_list.append(S[-character])

        for character in range(len(S)):
            # checking if character is numeric
            if S[character].isalpha() == False:
                # cut the reversed_list in left and right sides
                # add the numeric character in the middle
                left_side = reversed_list[:character]
                right_side = reversed_list[character:]
                reversed_list = left_side + list(S[character]) + right_side

        # join every element of the reversed_list
        return "".join(reversed_list)
