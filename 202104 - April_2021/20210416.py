"""
Remove All Adjacent Duplicates in String II
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        last_seem = [" "]
        counter = [1]
        s_new=-1
        output = ""

        for i in range(len(s)):
            output += s[i]
            if s[i] != last_seem[-1]:
                last_seem.append(s[i])
                counter.append(1)
            else:
                counter[-1] += 1

                if counter[-1] == k:
                    output = output[:- k]
                    last_seem.pop()
                    counter.pop()

        return output