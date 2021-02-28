"""
997. Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.


"""


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        potential_judges = []  # store potential judges

        # N is the total number of people involved
        # for each person, assign a variable trust_count
        for i in range(1, N + 1):
            trust_count = 0
            # for each pair of people, if the person i is on the right side of the list
            # increase trus_count because the person on the left trust the person on the right
            for pair in trust:
                if pair[1] == i:
                    trust_count += 1

            # if the trust_count of a person i is equal to N-1
            # and if person i is not in the list of potential judges
            # add the person i to the list of potential judges
            # the judge's trust_count should be equal to N-1 because everyone (N people)
            # should trust the judge minus the judge himself
            if trust_count == N - 1:
                if i not in potential_judges:
                    potential_judges.append(i)

        # if any of the potential judges trust someone, substitute the judge by -1
        for j in range(len(potential_judges)):
            for i in range(len(trust)):
                if potential_judges[j] == trust[i][0]:
                    potential_judges[j] = -1

        # for any judge in the list of potential judges, check if it is different from -1
        # if so, return the judge
        for j in range(len(potential_judges)):
            if potential_judges[j] != -1:
                return potential_judges[j]

        return -1