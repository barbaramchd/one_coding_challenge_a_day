class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def intersection(lst1, lst2):
            lst3 = [value for value in lst1 if value in lst2]
            return lst3

        zeros_dict = {}
        ones_dict = {}
        for digit in strs:
            zeros_dict[digit] = digit.count("0")
            ones_dict[digit] = digit.count("1")

        zeros_dict_sorted = {k: v for k, v in sorted(zeros_dict.items(), key=lambda item: item[1])}
        ones_dict_sorted = {k: v for k, v in sorted(ones_dict.items(), key=lambda item: item[1])}

        subset_counter_zeros = {}
        zeros_counter = list(zeros_dict_sorted.items())[0][1]
        for key in zeros_dict_sorted:
            if m >= zeros_counter:
                subset_counter_zeros.append(key)
                zeros_counter += zeros_dict_sorted[key]

        subset_counter_ones = {}
        ones_counter = list(ones_dict_sorted.items())[0][1]
        for key in ones_dict_sorted:
            if n >= ones_counter:
                subset_counter_ones.append(key)
                ones_counter += ones_dict_sorted[key]

        print("zero:", subset_counter_zeros)
        print("one:", subset_counter_ones)
        if m <= n:
            return len(intersection(subset_counter_zeros, subset_counter_ones))
        else:
            return len(intersection(subset_counter_zeros, subset_counter_ones))


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def intersection(lst1, lst2):
            lst3 = [value for value in lst1 if value in lst2]
            return lst3

        zeros_dict = {}
        ones_dict = {}
        for digit in strs:
            zeros_dict[digit] = digit.count("0")
            ones_dict[digit] = digit.count("1")

        zeros_dict_sorted = {k: v for k, v in sorted(zeros_dict.items(), key=lambda item: item[1])}
        ones_dict_sorted = {k: v for k, v in sorted(ones_dict.items(), key=lambda item: item[1])}

        subset_counter_zeros = {}
        zeros_counter = list(zeros_dict_sorted.items())[0][1]
        for key in zeros_dict_sorted:
            if m >= zeros_counter:
                subset_counter_zeros[key] = digit.count("1")
                zeros_counter += zeros_dict_sorted[key]

        subset_counter_ones = {}
        ones_counter = list(ones_dict_sorted.items())[0][1]
        for key in ones_dict_sorted:
            if n >= ones_counter:
                subset_counter_ones[key] = digit.count("0")
                ones_counter += ones_dict_sorted[key]

        final_zeros_dict_sorted = {k: v for k, v in sorted(subset_counter_zeros.items(),
                                                           key=lambda item: item[1])}
        final_ones_dict_sorted = {k: v for k, v in sorted(subset_counter_ones.items(),
                                                          key=lambda item: item[1])}
        final_subset_counter_zeros = []
        final_zeros_counter = list(final_zeros_dict_sorted.items())[0][1]
        for key in final_zeros_dict_sorted:
            if n >= final_zeros_counter:
                final_subset_counter_zeros.append(key)
                final_zeros_counter += final_zeros_dict_sorted[key]

        final_subset_counter_ones = []
        final_ones_counter = list(final_ones_dict_sorted.items())[0][1]
        for key in final_ones_dict_sorted:
            if m >= final_ones_counter:
                final_subset_counter_ones.append(key)
                final_ones_counter += final_ones_dict_sorted[key]

        if m <= n:
            return len(intersection(final_subset_counter_zeros, final_subset_counter_ones))
        else:
            return len(intersection(final_subset_counter_zeros, final_subset_counter_ones))


