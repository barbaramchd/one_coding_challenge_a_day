"""
Sudoku Solver
"""
digits = '123456789'
rows = 'ABCDEFGHI'
columns = digits


def cross(X, Y):
    """"
    Creates cross product of elements in X and in Y.

    """

    # stores the cross products
    combinations = []

    for x in X:
        for y in Y:
            combinations.append(x + y)

    # return a list of all the cross products
    return combinations


# list with all coordinates for each square
squares = cross(rows, columns)

# list all row units
row_units = [cross(row, columns) for row in rows]

# list of all column units
column_units = [cross(rows, column) for column in columns]

# list of all block units
block_units = [cross(rs, columns) for rs in ('ABC', 'DEF', 'GHI') for columns in ('123', '456', '789')]

# list of all units
unit_list = (row_units + column_units + block_units)


def map_square_units(squares, unit_list):
    """
    Creates a dict that maps each square to the list of units that contain
    that square. Note that each square has 3 units: its rown, its column,
    and its block.
    """
    unit_dict = {}
    for square in squares:
        for unit in unit_list:
            if square in unit:
                if square not in unit_dict:
                    unit_dict[square] = []

                unit_dict[square].append(unit)

    return unit_dict


square_units = map_square_units(squares, unit_list)


def map_peers(squares, square_units):
    """
    Creates a dict where each square maps to the set of its peers.
    Note that peers is the all the squares that share the unit with the
    square in question, but not the square itself.
    """
    peers_dict = {}
    for square in squares:
        peers_dict[square] = set()

        for l in square_units[square]:
            united_sets = peers_dict[square].union(set(l))
            peers_dict[square] = united_sets - set([square])

    return peers_dict


peers = map_peers(squares, square_units)


def diag_squares(row_units, column_units):
    """
    Create a list with two lists. The first list contains the numbers
    in the diagonal from left to right. The second list contains the numbers
    in the diagonal from right to left.
    """
    diag_list1 = []
    diag_list2 = []
    for i in range(len(row_units)):
        diag_list1.append(row_units[i][i])
        diag_list2.append(row_units[i][-i - 1])

    return [diag_list1, diag_list2]


diag_list = diag_squares(row_units, column_units)


def parse_sudoku(board):
    """
    Convert sudoku board to a dict of possible values, {square: values}.
    We sign the values '0' or '.' as empty squares."
    """

    square_values = []
    for element in board:
        if element.isnumeric():
            if element == "0" or element == ".":
                square_values.append('123456789')
            else:
                square_values.append(element)

    values = dict(zip(squares, square_values))

    return values


def only_choice_strategy(values):
    """
    Check all the units, and if there is a unit with a value that can only be
    placed to one specific square, assign the value to the square.
    Input:
        values - Sudoku board in dictionary datatype.
    Output:
        values - Resulting sudoku board in dict format after
        filling in only choices.
    """
    for unit in unit_list:
        for number in digits:
            # find the a list of potential squares that can handle a value
            potential_squares = []
            for square in unit:
                if number in values[square]:
                    potential_squares.append(square)

            # if there is only one potential square that can handle a value
            # it means that the value SHOULD be placed in that square
            if len(potential_squares) == 1:
                values[potential_squares[0]] = number

    return values


def eliminate_strategy(values):
    """
    Go through all the squares, and when there is a solved square
    (meaning a square with length 1 or with a single value), eliminate this
    value from the set of values of all its peers (including diagonal peers).
    Input:
        values - Sudoku board in dictionary datatype.
    Output:
        values - Resulting sudoku board in dict format after eliminated values.
    """

    # list with all solved squares
    solved_squares = []
    for square in values:
        if len(values[square]) == 1:
            solved_squares.append(square)

    # check if the values in the solved squares lists also appear in the
    # peers. If so, take the value out.
    for solved_square in solved_squares:
        for peer in peers[solved_square]:
            values[peer] = values[peer].replace(values[solved_square], '')
            # if len(values[peer]) == 0:
            #    return False ## Contradiction: removed last value

        # if there is a square on the diagonal with a single value,
        # eliminate the value from the list of possible values
        # of the diagonal peers
        for diag_squares in diag_list:
            if solved_square in diag_squares:
                for diag_square in diag_squares:
                    if diag_square != solved_square:
                        values[diag_square] = values[diag_square].replace(values[solved_square], '')

    # note that we already callend the Naked Twins function
    # This strategy will be further explained bellow.
    return naked_twins_strategy(values)


def reduce_sudoku(values):
    """
    This function reduces the number of options for each square by using
    the Eliminate Strategy and the Only Choice Strategy

    Input:
        Sudoku board in dict format.
    Output:
        Reduced sudoku board in dict format.
    """

    no_changes = False
    while not no_changes:
        solved_squares1 = 0
        for square in values:
            if len(values[square]) == 1:
                solved_squares1 += 1

        values = eliminate_strategy(values)
        values = only_choice_strategy(values)

        solved_squares2 = 0
        for square in values:
            if len(values[square]) == 1:
                solved_squares2 += 1

        # if we can't find new values, sign that we we cant find new changes
        # and stop looping
        if solved_squares1 == solved_squares2:
            no_changes = True

        for square in values:
            # if at least one square is empty
            # the solution doesnt exist in this branch of the tree
            if len(values[square]) == 0:
                return False

    return values


def naked_twins_strategy(values):
    """
    Find two squares, both in the same unit, that have only the
    same two candidate values left, and eliminate that two possible values
    from all the peers of the squares.

    Input:
        Sudoku board in dict format.
    Output:
        Sudoku board in dict format with the twins eliminated from peers.
    """

    # find coordinates of naked twins
    total_unit_list = diag_list + unit_list
    for unit in total_unit_list:
        naked_dict = {}
        for square in unit:
            if values[square] not in naked_dict:
                naked_dict[values[square]] = []
            naked_dict[values[square]].append(square)
        # eliminate the naked twins as possible candidates for their peers
        for digit_key in naked_dict:
            coordinate = naked_dict[digit_key]
            if len(coordinate) == 2 and len(digit_key) == 2:
                for square in unit:
                    if square not in naked_dict[digit_key]:
                        for d in digit_key:
                            values[square] = values[square].replace(d, '')
    return values


def depth_first_search(values):
    """
    Choose unfilled squares and use depth-first search and propagation
    to try all possible values.
    """

    # to avoid a too big tree, we will first reduce the search space of the
    # puzzle by using the strategies that we defined previously
    values = reduce_sudoku(values)
    if not values:
        return False

    solved = True
    for square in squares:
        # if all squares have just one value, it means that
        # we solved the puzzle!
        if len(values[square]) != 1:
            solved = False

    if solved == True:
        return values

    # Chose the blank square s with the fewest possible
    # number of candidate values
    len_min_square = float('inf')
    min_seem_square = ''
    for square in squares:
        if len(values[square]) > 1:
            if len_min_square > len(values[square]):
                min_seem_square = square
                len_min_square = len(values[square])

    # create a copy of the puzzle because the branchs of the tree must be
    # independent. Then, we try to solve by calling search function
    # recursively. If we there is a solution, return the puzzle solved
    for value in values[min_seem_square]:
        new_puzzle = values.copy()
        new_puzzle[min_seem_square] = value
        solving_try = depth_first_search(new_puzzle)
        if bool(solving_try) == True:
            return solving_try