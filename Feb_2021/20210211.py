"""
771. Jewels and Stones
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

# SOLUTION 1
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for j in range(len(jewels)):
            for s in range(len(stones)):
                if jewels[j] == stones[s]:
                    counter += 1
        return counter


# SOLUTION 2
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for s in range(len(stones)):
            if stones[s] in jewels:
                counter += 1
        return counter
