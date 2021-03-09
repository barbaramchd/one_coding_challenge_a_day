"""
Implementing A* search in a N-Puzzle solver
"""


# Import any packages you need here
# Also define any variables as needed

# YOUR CODE HERE (OPTIONAL)

# Now, define the class PuzzleNode:
class PuzzleNode:
    """
    Class PuzzleNode: Provides a structure for performing A* search for the n^2-1 puzzle
    """

    def __init__(self, state, parent=None, children=[], g=0, total_cost=0):

        self.state = state
        self.parent = parent
        self.children = children
        self.g = g  # path cost from the start node to node n
        self.total_cost = total_cost  # path_cost + heuristic cost
        self.pruned = False  # flags if node was pruned

        flat_list_current_state = []
        for sublist in self.state:
            flat_list_current_state += sublist
        flat_list_current_state = map(str, flat_list_current_state)
        self.str = "".join(flat_list_current_state)

    def __len__(self):
        """
        len method: implements length for the Puzzle node
        """
        return (len(self.state)) ** 2

    def __lt__(self, other):
        """
        lt method: allows comparisson "<" between the nodes. Required for the heap.
        """
        return self.total_cost < other.total_cost

    def __repr__(self):
        """
        repr method: nicely prints the current node, frontier, visited nodes, and any other variable defined.
        """
        flat_list_current_state = []
        for sublist in self.state:
            flat_list_current_state += sublist
        flat_list_current_state = map(str, flat_list_current_state)
        return "".join(flat_list_current_state) + " " + str(self.g) + " " + str(self.total_cost) + " " + str(
            self.pruned)

    ### HEURISTICS
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
        str_state = "".join(map(str, flat_list_current_state))
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
        str_state = "".join(map(str, flat_list_current_state))
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
                    goal_row, goal_col = state[row][column] // n, state[row][column] % n
                    manhattan_dist += abs(row - goal_row) + abs(column - goal_col)

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
        str_state = "".join(map(str, flat_list_current_state))
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
                # jumps to the next iteration
                goal_row, goal_col = state[row][column] // n, state[row][column] % n
                if [row, column] == [goal_row, goal_col]:
                    continue

                # if element is in its correct column
                if column == goal_col:
                    # if elements is on the right of its goal_row position
                    if row + 1 < goal_row:
                        # for all the remaining positions on the column
                        for j in range(row + 1, len(state)):
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
                    if column + 1 < goal_col:
                        # for all the remaining positions on the row
                        for i in range(column + 1, len(state)):
                            # if current element is larger than the other elements
                            # on the remaining positions
                            if state[row][column] > state[row][i]:
                                # if element on the remaining positions are different form zero
                                if state[row][i] != 0:
                                    # if element on the remaining positions is on the correct row
                                    if state[row][i] in (row * n + np.arange(n)):
                                        # increases linear_conflicts counter
                                        linear_conflicts += 1

        dict_cache_h3[str_state] = 2 * linear_conflicts + h2(state)
        return 2 * linear_conflicts + h2(state)

    # If you implement more than 3 heuristics, then add any extra heuristic functions onto the end of this list.
    heuristics = [h1, h2, h3]

    ### A* SEARCH
    import heapq
    import copy
    import numpy as np

    def generate_states(state, n, node):
        """
        This function generates all the possible children for a given state
        and checks if child was not generated in the step before.
        Input:
            -state: the board state as a list of lists
            - n: dimension of the puzzle
            - node: the state of the previous node
        Output:
            -children_nodes: list of nodes of all possible children
        """

        # searching for row and column of the empty tile
        for row in range(len(state)):
            for column in range(len(state[row])):
                if state[row][column] == 0:
                    empty_tile_row, empty_tile_column = row, column

        children = []

        # if empty tile is not on the left edge of the board
        if empty_tile_column > 0:
            # copy child
            child = copy.deepcopy(state)
            # swap the empty tile with the tile on the left
            child[empty_tile_row][empty_tile_column] = child[empty_tile_row][empty_tile_column - 1]
            child[empty_tile_row][empty_tile_column - 1] = 0
            # append child
            children.append(child)

        # if empty tile is not on the right edge of the board
        if empty_tile_column < n - 1:
            # copy child
            child = copy.deepcopy(state)
            # swap the empty tile with the tile on the right
            child[empty_tile_row][empty_tile_column] = child[empty_tile_row][empty_tile_column + 1]
            child[empty_tile_row][empty_tile_column + 1] = 0
            # append child
            children.append(child)

        # if empty tile is not on the top edge of the board
        if empty_tile_row > 0:
            # copy child
            child = copy.deepcopy(state)
            # swap the empty tile with the tile on the top
            child[empty_tile_row][empty_tile_column] = child[empty_tile_row - 1][empty_tile_column]
            child[empty_tile_row - 1][empty_tile_column] = 0
            # append child
            children.append(child)

        # if empty tile is not on the bottom edge of the board
        if empty_tile_row < n - 1:
            # copy child
            child = copy.deepcopy(state)
            # swap the empty tile with the tile on the top
            child[empty_tile_row][empty_tile_column] = child[empty_tile_row + 1][empty_tile_column]
            child[empty_tile_row + 1][empty_tile_column] = 0
            # append child
            children.append(child)

        # transforming each element in list children_nodes
        # into a node, except the previous node
        children_nodes = []
        for child in children:
            if child != node:
                children_nodes.append(PuzzleNode(child))

        return children_nodes

    def opt_path(node):
        """
        This function returns the optimal path to solve a give board state
        by going backwards on the node visited.
        Input:
            -node: the last node of a state. Could be the solved state.
        Output:
            -path: list of states
        """
        # if it is not an istance
        # return the state
        if not isinstance(node.parent, PuzzleNode):
            return [node.state]

        # else, go backwards on the node by looking the parents
        # append the parents to path
        # return path
        else:
            path = opt_path(node.parent)
            path.append(node.state)
            return path

    # Main solvePuzzle function.
    def solvePuzzle(state, heuristic):
        """This function should solve the n**2-1 puzzle for any n > 2 (although it may take too long for n > 4)).
        Inputs:
            -state: The initial state of the puzzle as a list of lists
            -heuristic: a handle to a heuristic function.  Will be one of those defined in Question 2.
        Outputs:
            -steps: The number of steps to optimally solve the puzzle (excluding the initial state)
            -exp: The number of nodes expanded to reach the solution
            -max_frontier: The maximum size of the frontier over the whole search
            -opt_path: The optimal path as a list of list of lists.  That is, opt_path[:,:,i] should give a list of lists
                        that represents the state of the board at the ith step of the solution.
            -err: An error code.  If state is not of the appropriate size and dimension, return -1.  For the extention task,
              if the state is not solvable, then return -2
        """
        result = {
            "steps": 0,
            "exp": 0,
            "max_frontier": 0,
            "opt_path": None,
            "err": 0
        }

        # define the dimensions of the puzzle as the number of the rows
        # if the number of rowns and columns dont match, i will return an error
        state_dimension = len(state)

        # store a flat list of the current state
        flat_list_current_state = []
        for sublist in state:
            flat_list_current_state += sublist

        # if the state does not contain every number from 0 to (n^2)-1
        # set err to -1
        for number in range((state_dimension ** 2)):
            if number not in flat_list_current_state:
                result["err"] = -1
                return result["steps"], result["exp"], result["max_frontier"], result["opt_path"], result["err"]

        # if number of columns and number of rows dont match
        # set err to -1
        for row in state:
            if len(row) != state_dimension:
                result["err"] = -1
                return result["steps"], result["exp"], result["max_frontier"], result["opt_path"], result["err"]

        # starting the queue/frontier
        current_node = PuzzleNode(state=state)
        frontier = []
        heapq.heapify(frontier)
        # starting the visited_nodes
        visited_nodes = [PuzzleNode([[0, 0, 0], [0, 0, 0], [0, 0, 0]])]
        visited_strings = {}

        # while the heuristic doenst return 0
        while heuristic(current_node.state) != 0:

            # we dont want prunned nodes
            if current_node.pruned:
                continue

            # generate all the possible children of the current node
            current_node.children = generate_states(current_node.state, state_dimension, visited_nodes[-1].state)
            # for each child
            for child in current_node.children:
                # child's g cost will be the cost of its parent + 1
                child.g = current_node.g + 1
                # total cost equals g cost + heuristic's cost
                child.total_cost = child.g + heuristic(child.state)
                # current node is now the parent node of the children
                child.parent = current_node

                # Check if we already have a child in visited or frontier
                # And add only if missing or smaller
                found = False
                if child.str in visited_strings:
                    found = True
                    if visited_strings[child.str] > child.g:
                        heapq.heappush(frontier, child)

                # else, push the child to the frontier
                else:
                    heapq.heappush(frontier, child)

            # Creating a copy of visited that stores string representation
            # of current node, because dictionary has average time complexity
            # O(1) for checking if key exists
            visited_strings[current_node.str] = current_node.g
            # appends current node to visited nodes
            visited_nodes.append(current_node)

            # increase the number of nodes expanded during search
            result["exp"] += 1

            # if frontier is empty
            # returns err -2
            if len(frontier) == 0:
                result["err"] = -2
                return result["steps"], result["exp"], result["max_frontier"], result["opt_path"], result["err"]
                break

            # pop current node from the frontier
            # because i am this node from the frontier
            # for the next iteration
            current_node = heapq.heappop(frontier)

            # if length of frontier is larger than the previous
            # length of frontier
            # updates result["max_frontier"]
            if len(frontier) > result["max_frontier"]:
                result["max_frontier"] = len(frontier)

        # calls opt_path function
        result["opt_path"] = opt_path(current_node)

        # steps equals to the length of the optimal path minus 1
        # because we dont count the initial state
        result["steps"] = len(opt_path(current_node)) - 1

        return result["steps"], result["exp"], result["max_frontier"], result["opt_path"], result["err"]