"""
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing = []  # store all the numbers that are self dividing
        for i in range(left, right + 1):  # must be inclusive range
            new_i = str(i)  # need to transform integer in str to get its length
            for j in range(len(new_i)):
                # set a variable to control if we have finished checking for all elements
                # in the string
                finished = False
                # if the element is not equal to "0"
                if new_i[j] != "0":
                    # convert it back to integer so I can use %
                    divisor = int(new_i[j])
                    # if there is rest in the divison, break
                    if i % divisor != 0:
                        break
                    else:
                        # if not, change the control variable
                        finished = True
                else:
                    # if the element equals "0", break
                    break
            if finished:
                # if we have finished checking for all elements of the number, append
                self_dividing.append(i)

        return self_dividing
