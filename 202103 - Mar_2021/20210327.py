"""
1323. Maximum 69 Number
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""
#SOLUTION 1: USING STRING
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            output = ""
            if num[i] == "6":
                first_part = num[:i]
                output += first_part
                output += "9"
                second_part = num[i+1:]
                output += second_part
                output_num = int(output)
                return output_num
        return num

#SOLUTION 2: LESS LINES OF CODE
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            if num[i] == "6":
                return int(num[:i] + "9" + num[i+1:])
        return num