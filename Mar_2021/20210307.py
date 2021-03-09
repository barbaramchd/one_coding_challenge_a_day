import numpy as np

# Memoization method: saves all the states and quickly
# finds it in the dictionary if it was already computed
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

    global dict_cache_h1

    # store a flat list of the current state
    flat_list_current_state = []
    for sublist in state:
        flat_list_current_state += sublist

    # create a string representation of my current state
    # so I can have an hashable key for dictionary
    str_state = "".join(map(str,flat_list_current_state))
    if str_state in dict_cache_h1:
        return dict_cache_h1[str_state]

    # initializing misplaced tiles counter
    misplaced_tiles = 0
    sorted_tiles = sorted(flat_list_current_state)
    # if element in position i is different from element in position i
    # in sorted current state, increase misplaced_tiles counter
    # if it 0 just jumps to the next iteration
    for i in range(len(flat_list_current_state)):
        if flat_list_current_state[i] != sorted_tiles[i]:
            if flat_list_current_state[i] == 0:
                continue
            else:
                misplaced_tiles += 1

    # saving result to the dictionary
    dict_cache_h1[str_state] = misplaced_tiles

    # return misplaced tiles value
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

    global dict_cache_h2

    # store a flat list of the current state
    flat_list_current_state = []
    for sublist in state:
        flat_list_current_state += sublist

    # create a string representation of my current state
    # so I can have an hashable key for dictionary
    str_state = "".join(map(str,flat_list_current_state))
    if str_state in dict_cache_h2:
        return dict_cache_h2[str_state]

    # n is the dimension of the puzzle
    n = len(state)

    # initializing manhattan distance counter
    manhattan_dist = 0

    # for each element of each row, checks if the element is zero
    # if not zero, calculates the manhattan distance
    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == 0:
                continue

            else:
                goal_row,goal_col = state[row][column]//n,state[row][column] % n
                manhattan_dist += abs(row-goal_row) + abs(column - goal_col)

    # saving result to the dictionary
    dict_cache_h2[str_state] = manhattan_dist

    # return value of manhattan distance
    return manhattan_dist

# Extra heuristic for the extension.  If implemented, modify the function below
def h3(state):
    """
    The linear-conflict heuristic applies when two tiles are in their goal row or column,
    but are reversed relative to their goal positions (Hansson, Mayer & Yung, 1992).
    For example, if the first row of an 8- puzzle contains the tiles (2 1) in that order,
    to reverse them, one of the tiles must move down out of the top row, to allow the
    other to pass by, and then back up. Since these two moves are not counted in
    the Manhattan distance of either tile, two moves can be added (Korf & Taylor, 1996).
    Input:
        -state: the board state as a list of lists
    Output:
        -h: the Heuristic distance of the state from its solved configuration
    """
    global dict_cache_h3

    # store a flat list of the current state
    flat_list_current_state = []
    for sublist in state:
        flat_list_current_state += sublist

    # create a string representation of my current state
    # so I can have an hashable key for dictionary
    str_state = "".join(map(str,flat_list_current_state))
    if str_state in dict_cache_h3:
        return dict_cache_h3[str_state]

    # n is the dimmension of the puzzle
    n = len(state)

    # initializing linear conflicts counter
    linear_conflicts = 0

    # checks if each element of each row
    for row in range(len(state)):
        for column in range(len(state[row])):

            # checks if element is zero
            # if so, jumps to the next iteration
            if state[row][column] == 0:
                continue

            # if element is already on its correct position
            # meaning on its correct column and row
            #jumps to the next iteration
            goal_row,goal_col = state[row][column]//n,state[row][column] % n
            if [row, column] == [goal_row,goal_col]:
                continue

            # if element is in its correct column
            if column == goal_col:
                # if elements is on the right of its goal_row position
                if row+1 < goal_row:
                    # for all the remaining positions on the column
                    for j in range(row+1, len(state)):
                        # if current element is larger than the other elements
                        # on the remaining positions
                        if state[row][column] > state[j][column]:
                            # if element on the remaining positions are different from zero
                            if state[j][column] != 0:
                                # if element on the remaining positions is on the correct column
                                if state[j][column] in (column + n * np.arange(n)):
                                    # increases linear_conflicts counter
                                    linear_conflicts += 1

            # if element is in its correct row
            elif row == goal_row:
                # if elements is on the bottom of its goal_column position
                if column+1 < goal_col:
                    # for all the remaining positions on the row
                    for i in range(column+1, len(state)):
                        # if current element is larger than the other elements
                        # on the remaining positions
                        if state[row][column] > state[row][i]:
                            # if element on the remaining positions are different form zero
                            if state[row][i] != 0:
                                 # if element on the remaining positions is on the correct row
                                if state[row][i] in (row * n + np.arange(n)):
                                    # increases linear_conflicts counter
                                    linear_conflicts += 1


    dict_cache_h3[str_state] = 2*linear_conflicts + h2(state)
    return 2*linear_conflicts + h2(state)

# If you implement more than 3 heuristics, then add any extra heuristic functions onto the end of this list.
heuristics = [h1, h2, h3]