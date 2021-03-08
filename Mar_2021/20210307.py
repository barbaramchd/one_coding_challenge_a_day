"""
3 Heuristics to solve the N-Puzzle
"""
import numpy as np

dict_cache_h1 = {}
dict_cache_h2 = {}
dict_cache_h3 = {}


# Misplaced tiles heuristic
def h1(state):
    """
    This function returns the number of misplaced tiles, given the board state
    Input:
        -state: the board state as a list of lists
    Output:
        -h: the number of misplaced tiles
    """
    # store a flat list of the current state
    flat_list_current_state = []
    for sublist in state:
        flat_list_current_state += sublist

    str_state = "".join(map(str,flat_list_current_state))
    if str_state in dict_cache_h1:
        return dict_cache_h1[str_state]

    misplaced_tiles = 0
    sorted_tiles = sorted(flat_list_current_state)
    for i in range(len(flat_list_current_state)):
        if flat_list_current_state[i] != sorted_tiles[i]:
            if flat_list_current_state[i] == 0:
                continue
            else:
                misplaced_tiles += 1
    dict_cache_h1[str_state] = misplaced_tiles
    return misplaced_tiles


# Manhattan distance heuristic
def h2(state):
    """
    This function returns the Manhattan distance from the solved state, given the board state
    Input:
        -state: the board state as a list of lists
    Output:
        -h: the Manhattan distance from the solved configuration
    """
    n = len(state)
    manhattan_dist = 0
    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == 0:
                continue

            else:
                goal_row, goal_col = state[row][column] // n, state[row][column] % n
                manhattan_dist += abs(row - goal_row) + abs(column - goal_col)
    return manhattan_dist


# Extra heuristic for the extension.  If implemented, modify the function below
def h3(state):
    """
    This function returns a heuristic that dominates the Manhattan distance, given the board state
    Input:
        -state: the board state as a list of lists
    Output:
        -h: the Heuristic distance of the state from its solved configuration
    """
    n = len(state)
    linear_conflicts = 0
    for row in range(len(state)):
        for column in range(len(state[row])):

            if state[row][column] == 0:
                continue

            goal_row, goal_col = state[row][column] // n, state[row][column] % n
            if [row, column] == [goal_row, goal_col]:
                continue

            if column == goal_col:
                if row + 1 < goal_row:
                    for j in range(row + 1, len(state)):
                        if state[row][column] > state[j][column]:
                            if state[j][column] != 0:
                                if state[j][column] in (column + n * np.arange(n)):
                                    linear_conflicts += 1

            elif row == goal_row:
                if column + 1 < goal_col:
                    for i in range(column + 1, len(state)):
                        if state[row][column] > state[row][i]:
                            if state[row][i] != 0:
                                if state[row][i] in (row * n + np.arange(n)):
                                    linear_conflicts += 1

    return 2 * linear_conflicts + h2(state)


# If you implement more than 3 heuristics, then add any extra heuristic functions onto the end of this list.
heuristics = [h1, h2, h3]