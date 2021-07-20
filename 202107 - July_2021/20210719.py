"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


"""


class Solution:
    def reverse(self, x: int) -> int:

        if x >= 2 ** 31 - 1:
            return 0

        elif x <= -2 ** 31:
            return 0

        else:
            x = str(x)
            x_str = ""
            if x[0] == "-":
                x_str += x[0]

            for num in reversed(x):
                if num != "-":
                    x_str += num
            x_num = int(x_str)
            if x_num >= 2 ** 31 - 1 or x_num <= -2 ** 31:
                return 0
            else:
                return x_num