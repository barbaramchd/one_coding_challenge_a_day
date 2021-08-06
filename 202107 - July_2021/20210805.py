"""
  Stone Game

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.
"""


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # variables to keep track of Alex and Lee scores
        alex_score = 0
        lee_score = 0

        # while there is a stone at the pile
        while piles:
            # alex plays optimally and starts the game, so he gets
            # the largest value
            alex_score += max(piles)
            # then we remove the value
            piles.remove(max(piles))
            # return the same process
            lee_score += max(piles)
            piles.remove(max(piles))

        # if alex's score  is larger than lee's score
        # return true
        return alex_score > lee_score