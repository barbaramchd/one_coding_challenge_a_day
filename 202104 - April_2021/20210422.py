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

row_units = [cross(row, columns) for row in rows]

column_units = [cross(rows, column) for column in columns]

block_units = [cross(rs, columns) for rs in ('ABC', 'DEF', 'GHI') for columns in ('123', '456', '789')]

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

square_units