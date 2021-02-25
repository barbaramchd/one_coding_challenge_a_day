"""
412. Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []
        for number in range(1, n + 1):
            if number % 3 == 0 and number % 5 == 0:
                results.append("FizzBuzz")
            elif number % 5 == 0:
                results.append("Buzz")
            elif number % 3 == 0:
                results.append("Fizz")
            else:
                results.append(str(number))

        return results
