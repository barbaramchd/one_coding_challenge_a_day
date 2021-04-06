"""
  Global and Local Inversions
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.
"""
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        local_inv = 0
        global_inv = 0
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                local_inv += 1

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    global_inv += 1
                    if global_inv > local_inv:
                        return False

        if global_inv == local_inv:
            return True
        else:
            return False
