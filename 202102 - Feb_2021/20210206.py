"""
1688. Count of Matches in Tournament
You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.
"""

# SOLUTION 1
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matchesCount = 0
        if n == 1:
            return matchesCount
        while n > 2:
            if n % 2 == 0:
                matchesCount += n / 2
                n = n / 2
            else:
                matchesCount += (n - 1) / 2
                n = (n - 1) / 2 + 1
        return int(matchesCount + 1)


# SOLUTION 2
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matchesCount = 0
        if n == 1:
            return matchesCount
        if n ==2:
            return matchesCount +1
        if n%2 ==0:
            matchesCount += n/2
            return int(self.numberOfMatches(n/2) + matchesCount)
        else:
            matchesCount += (n - 1) / 2
            return int(self.numberOfMatches((n - 1) / 2 + 1) + matchesCount)