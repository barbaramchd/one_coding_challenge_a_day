"""
551. Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.
"""
class Solution:
    def checkRecord(self, s: str) -> bool:
        rewarded = True  # start as being rewarded
        A_counts = 0  # count of A occurrences
        L_counts = 0  # count of L occurrences
        for character in range(len(s)):
            if s[character] == "A":
                A_counts += 1
            if s[character] == "L":
                L_counts += 1
            if s[character] != "L":
                L_counts = 0
            if A_counts > 1 or L_counts > 2:
                rewarded = False

        return rewarded