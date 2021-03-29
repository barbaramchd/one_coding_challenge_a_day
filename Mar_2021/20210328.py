class Literal:
    def __init__(self, name, sign=True):
        self.name = name
        self.sign = sign

    def __neg__(self):
        return (Literal(self.name, sign=not self.sign))

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name


def clause_evaluation(clause, sat_model):
    for symbol in clause:
        if not (symbol.sign ^ sat_model[symbol]) == True:
            return True
    return False


def degree_heuristic(KB, sat_model):
    symbols_dict = {}
    for clause in KB:
        for symbol in clause:
            if symbol not in symbols_dict:
                symbols_dict[symbol] = 1
            else:
                symbols_dict[symbol] += 1

    max_count_symbol = -float('inf')
    max_symbol = None
    for key in symbols_dict:
        if key not in sat_model:
            if symbols_dict[key] > max_count_symbol:
                max_count_symbol = symbols_dict[key]
                max_symbol = key
            elif symbols_dict[key] == max_count_symbol:
                if ord(max_symbol.name) > ord(key.name):
                    max_count_symbol = symbols_dict[key]
                    max_symbol = key

    return max_symbol


def pure_symbol_heuristic(KB, sat_model):
    pure_symbol_dict = {}
    trash_symbol = set()
    for clause in KB:
        for symbol in clause:
            if symbol not in pure_symbol_dict:
                if symbol.name not in trash_symbol:
                    pure_symbol_dict[symbol] = symbol.sign
            else:
                if symbol.sign != pure_symbol_dict[symbol]:
                    del pure_symbol_dict[symbol]
                    trash_symbol.add(symbol.name)

    pure_symbol = Literal('}')
    for key in pure_symbol_dict:
        if key not in sat_model:
            if ord(pure_symbol.name) > ord(key.name):
                pure_symbol = key

    if pure_symbol.name != "}":
        return pure_symbol
    else:
        return degree_heuristic(KB, sat_model)


def DPLL_Satisfiable(KB, heuristic_level=0):
    ''' satisfiable, model = DPLLSatisfiable(KB)
        Takes in a KB and returns whether the KB is satisfiable, and the model that makes it so

        KB: A knowledge base of clauses (CNF) consisting of a list of sets of literals.  A KB might look like
            [{A,B},{-A,C,D}]
        heuristic_level: An integer that will be passed in to specify which heuristics to implement
            (only for the extension activities).
        satisfiable: Returns True if the KB is satisfiable, or False otherwise
        Model: A dictionary that assigns a truth value to each literal for the model that satisfies KB.
            For example, a model might look like {A: True, B: False}
    '''
    symbols = set()
    for clause in KB:
        for symbol in clause:
            symbols.add(symbol)

    symbol_list = list(symbols)
    return DPLL(KB, symbol_list, heuristic_level)


symbol_trace = []


def DPLL(clauses, symbol_list, heuristic_level, sat_model={}, symbol_trace=[]):
    print(heuristic_level, sat_model, symbol_trace)
    try:
        for clause in clauses:
            # if a clause is False, we return False
            if clause_evaluation(clause, sat_model) == False:
                # print("false:",sat_model)
                return False, sat_model, symbol_trace
        # if every clause is true, we will return true
        # print(sat_model)
        return True, sat_model, symbol_trace

    except KeyError:
        # choose an unassigned literal at each step
        # and assign both true and false values to it
        # performing recursive evaluation of DPLL
        if heuristic_level == 0:
            for symbol in symbol_list:
                if symbol not in sat_model:
                    break

        elif heuristic_level == 1:
            symbol = degree_heuristic(KB, sat_model)

        elif heuristic_level == 2:
            symbol = pure_symbol_heuristic(KB, sat_model)

        sat_model_copy = sat_model.copy()
        sat_model_copy[symbol] = True
        symbol_trace.append(symbol)
        result_1 = DPLL(clauses, symbol_list, heuristic_level, sat_model_copy, symbol_trace)

        if result_1[0] == True:
            return result_1

        else:
            sat_model_copy = sat_model.copy()
            sat_model_copy[symbol] = False
            result_2 = DPLL(clauses, symbol_list, heuristic_level, sat_model_copy, symbol_trace)
            if result_2[0] == True:
                return result_2
            else:
                return result_1