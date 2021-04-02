"""
1323. Maximum 69 Number
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            output = 0
            if num[i] == "6":
                first_part = num[:i]
                second_part = num[i+1:]
                if first_part != "":
                    new_num = int(first_part) * 10**(len(num)-i)
                    output += new_num
                output += 9*10**(len(num)-1-i)
                if second_part != "":
                    output += int(second_part)
                return output
        return num