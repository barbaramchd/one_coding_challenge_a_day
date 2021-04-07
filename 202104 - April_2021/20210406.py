"""
  Minimum Operations to Make Array Equal

You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.
"""


class Solution:
    def minOperations(self, n: int) -> int:
        list_numbers = []
        for i in range(n):
            value = (2 * i) + 1
            list_numbers.append(value)

        differences = 0
        index = n // 2
        if n % 2 != 0:
            for i in range(index):
                if list_numbers[i] != list_numbers[index]:
                    differences += list_numbers[index] - list_numbers[i]
        else:
            average = sum(list_numbers) / len(list_numbers)
            for i in range(index):
                if list_numbers[i] != average:
                    differences += average - list_numbers[i]

        return int(differences)