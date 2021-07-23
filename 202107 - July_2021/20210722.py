"""
  Partition Array into Disjoint Intervals

Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.
"""


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # we assume that the partition between array left and right will be
        # at the position of the smallest numberof nums
        partition = self.find_min(nums)

        while True:

            left = nums[:partition + 1]  # assumed left array
            right = nums[partition + 1:]  # assumed right array

            # find the largest element on the left array
            max_left = max(left)
            done = True
            for r in range(len(right)):
                # if the largest element on the left array is larger
                # than any element on the right array
                # reset the partition point to be len(left) + r
                # or, reset it to the position of the smaller
                # number on the previous right array
                if max_left > right[r]:
                    partition = len(left) + r
                    done = False
                    break

            if done == True:
                return len(left)

    # function to find the position of the smallest element in an array
    def find_min(self, nums):
        min_num = float('inf')
        min_index = 0
        for num in range(len(nums)):
            if nums[num] < min_num:
                min_num = nums[num]
                min_index = num

        return min_index