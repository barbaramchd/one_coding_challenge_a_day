"""
1086. High Five
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.
"""

from collections import OrderedDict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students_dict = {}  # dict to store all the grades for each student
        for student in range(len(items)):
            # if student id is not already in the dict
            # create a new key with student's id an store the grade
            if items[student][0] not in students_dict:
                students_dict[items[student][0]] = [items[student][1]]

            # if student is already in the dict, just append the grade
            else:
                students_dict[items[student][0]].append(items[student][1])

        students_averages = {}  # dict to store the average of each student
        for key in students_dict:
            # sort the grades of each student
            students_dict[key] = sorted(students_dict[key], reverse=True)
            # average the top five best grades
            students_averages[key] = int(sum(students_dict[key][0:5]) / len(students_dict[key][0:5]))

            # order the dict according to student's id
        students_averages_ordered = dict(OrderedDict(sorted(students_averages.items(),
                                                            key=lambda t: t[0])))

        # return the student's average grades as a list of lists
        return list(students_averages_ordered.items())