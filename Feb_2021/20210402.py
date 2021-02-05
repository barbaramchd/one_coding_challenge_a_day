"""
1550. Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

"""
# Solution #1

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if len(arr[i + 1:]) >= 2:
                print("a: ", arr[i])
                print("b:", arr[i + 1])
                print("c:", arr[i + 2])
                if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                    return True
        return False

# Solution #2
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True
        return False