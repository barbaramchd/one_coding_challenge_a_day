"""
1470. Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
#SOLUTION1

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[n + i])

        return output


#SOLUTION2
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(n):
            output.append(nums[:n][i])
            output.append(nums[n:][i])

        return output

#SOLUTION3

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array1 = nums[:n]
        array2 = nums[n:]

        output = []
        for i in range(len(array1)):
            output.append(array1[i])
            output.append(array2[i])

        return output