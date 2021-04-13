"""
Beautiful Arrangement II

Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.
"""


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        counter1 = 1
        counter2 = n
        list1 = []

        for i in range(k):
            # if i is even
            if i % 2 == 0:
                list1.append(counter1)
                counter1 += 1
            # if i is odd
            else:
                list1.append(counter2)
                counter2 -= 1

        # if k is even
        if k % 2 == 0:
            rest_of_the_list = list(range(counter2, counter1 - 1, -1))
            list1 += rest_of_the_list
        # if k is odd
        else:
            rest_of_the_list = list(range(counter1, counter2 + 1, 1))
            list1 += rest_of_the_list

        return list1
