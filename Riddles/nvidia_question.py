import random
import sys
import numpy as np
import yaml


# This function helps test run function - and not relevant to the question
def test(n):
    val_array = np.zeros(n)
    title_arr = ['' for i in range(n)]
    title_arr[0] = 'p'
    for i in range(1, n):
        x = random.uniform(0, 1)
        if x < 0.2 or i == n - 1:
            title_arr[i] = 'p'
        else:
            title_arr[i] = 'd'
        val_array[i] = float(random.randint(1, 5))

    print(title_arr)
    print(val_array)
    run(title_arr, val_array)


'''
This function parses the yaml input file, assuming the input is correct The parsing works in the following way: 
given a correct file that defines len = n, the function returns two arrays of length n - cell_value_arr (beauty/num
coins in each cell) and cell_title_arr (princess or dragon) 
'''


def parse_input_file(file_name):
    with open(file_name) as file:
        input_str_arr = yaml.load(file, Loader=yaml.SafeLoader).split()
        array_len = int(input_str_arr[0])
        cell_title_arr = ['' for i in range(array_len)]
        # Entered first array value as a princess with beauty = 0, for comfort
        cell_value_arr = np.zeros(array_len)
        cell_title_arr[0] = 'p'
        try:
            for i in range(1, len(input_str_arr)):
                if input_str_arr[i] == 'd' or input_str_arr[i] == 'p':
                    cell_title_arr[int(i / 2) + 1] = input_str_arr[i]
                else:
                    cell_value_arr[int(i / 2)] = int(input_str_arr[i])
            return cell_title_arr, cell_value_arr
        except IndexError:
            print("Incorrect value entered as array length")
            return [], []


'''
index - an index of a princess in the input arrays
title_arr - cell_title_arr (input)
this functions returns the index of the previous princess
'''


def get_previous_princess_index(index, title_arr):
    for i in range(index - 1, 0, -1):
        if title_arr[i] == 'p':
            return i
    return 0


'''
cell_value_arr - a version of cell_value_array
num_dragons_allowed - a number of dragons the knight is allowed to kill
this function returns the indices of the dragons with most of the coins (bound by num_dragons_allowed)
'''


def get_best_dragon_combination(cell_value_arr, num_dragons_allowed):
    index_list = cell_value_arr.argsort()[int(-1 * num_dragons_allowed):][::-1]
    return index_list


'''
cell_title_arr - a version of cell_title_arr
this function counts the number of dragons in it, and returns the count
'''


def dragon_count(cell_title_arr):
    count = 0
    for i in cell_title_arr:
        if i == 'd':
            count += 1
    return count


'''
cell_value_arr - a version of cell_value_arr
cell_title_arr - a version of cell_title_arr
index_list - an index_list of dragon cells
prev_princess_index - the index of a previous princess
this function marks the following cells: all cells before prev_princess_index are marked if 
they are not in index_list or not a dragon, and the rest of the cells are marked if they are not a dragon
the mark is the lowest integer number (i'm assuming it won't be given as an input)
'''


def mark_elements(cell_value_arr, cell_title_arr, index_list, prev_princess_index):
    for i in range(len(cell_value_arr)):
        if i < prev_princess_index:
            if i not in index_list or cell_title_arr[i] == 'p':
                cell_value_arr[i] = sys.maxsize * -1
        else:
            if cell_title_arr[i] == 'p':
                cell_value_arr[i] = sys.maxsize * -1
    return cell_value_arr


# This as an explanation for calculate_princess_lower_bound(), calculate_princess_upper_bound(): the output array
# will hold for each princess two lists of indices - lower_bound: minimal number of dragons to kill, that maximize
# coin sum and allow marrying that princess upper_bound: maximal number of dragons to kill, that maximal coin sum and
# allow marrying that princess (without marrying previous princesses)

'''
prev_lower_bound - lower bound of the previous princess
cell_value_arr - a version of cell_value_arr
cell_title_arr - a version of cell_title_arr
i - current princess index
beauty_val - current princess beauty value
prev_princess_index - the index of a previous princess
this function returns the current princess lower_bound
'''


def calculate_princess_lower_bound(prev_lower_bound, cell_value_arr, cell_title_arr, i, beauty_val,
                                   prev_princess_index):
    # remove index that gives minimal coin value from prev_lower_bound
    left_hand_lower_bound = prev_lower_bound[:len(prev_lower_bound) - 1]
    # mark all princesses and dragons not in left_hand_lower_bound in cell_value_arr
    dragons_in_range = mark_elements(cell_value_arr[:i], cell_title_arr[:i], left_hand_lower_bound, prev_princess_index)
    potential_lower_bound = get_best_dragon_combination(dragons_in_range, beauty_val)
    lower_bound = np.array([])
    # get unmarked indices from potential_lower_bound
    for i in range(len(potential_lower_bound)):
        if cell_value_arr[int(potential_lower_bound[i])] != sys.maxsize * -1:
            lower_bound = np.append(lower_bound, int(potential_lower_bound[i]))
    return lower_bound


'''
prev_lower_bound - lower bound of the previous princess
cell_value_arr - a version of cell_value_arr
cell_title_arr - a version of cell_title_arr
dragon_count_in_range - number of dragons in between current princess and previous princess
i - current princess index
prev_princess_index - the index of a previous princess
this function returns the current princess upper_bound
'''


def calculate_princess_upper_bound(prev_lower_bound, cell_value_arr, cell_title_arr, dragon_count_in_range, i,
                                   prev_princess_index):
    # remove index that gives minimal coin value from prev_lower_bound
    left_hand_lower_bound = prev_lower_bound[:len(prev_lower_bound) - 1]
    # mark all princesses and dragons not in left_hand_lower_bound in cell_value_arr
    dragons_in_range = mark_elements(cell_value_arr[:i], cell_title_arr[:i], left_hand_lower_bound, prev_princess_index)
    potential_upper_bound = get_best_dragon_combination(dragons_in_range,
                                                        len(left_hand_lower_bound) + dragon_count_in_range)
    upper_bound = np.array([])
    # get unmarked indices from potential_upper_bound
    for i in range(len(potential_upper_bound)):
        if cell_value_arr[int(potential_upper_bound[i])] != sys.maxsize * -1:
            upper_bound = np.append(upper_bound, potential_upper_bound[i])
    return upper_bound


'''
i - current index in output array
cell_title_arr - a version of cell_title_arr
cell_value_arr - a version of cell_value_arr
output_array - this array contains the lower_bound and upper_bound for each princess
this function uses the previous functions and the previous cells of output_array to calculate
lower_bound and upper_bound of output_array[i], and returns it 
'''


def max_coins_per_index(i, cell_title_arr, cell_value_arr, output_array):
    copy_value_arr = np.copy(cell_value_arr)
    # first index no dragons seen yet
    if i == 0:
        return [], []
    else:
        # if cell is a dragon, do nothing
        if cell_title_arr[i] == 'p':
            # get prev_princess_index that it's lower_bound is not empty
            prev_princess_index = get_previous_princess_index(i, cell_title_arr)
            while len(output_array[prev_princess_index][0]) == 0 and prev_princess_index != 0:
                prev_princess_index = get_previous_princess_index(prev_princess_index, cell_title_arr)
            prev_lower_bound = output_array[prev_princess_index][0]
            dragons_in_range_title = cell_title_arr[prev_princess_index:i]
            # if there are not enough dragons between current princess and previous princess to marry current
            # princess, return empty bounds
            if len(prev_lower_bound) != 0 and \
                    len(prev_lower_bound) + dragon_count(dragons_in_range_title) - 1 < copy_value_arr[i]:
                return [], []
            elif len(prev_lower_bound) == 0 and dragon_count(dragons_in_range_title) < copy_value_arr[i]:
                return [], []

            # calculate bounds
            lower_bound = calculate_princess_lower_bound(prev_lower_bound, copy_value_arr, cell_title_arr,
                                                         i, copy_value_arr[i], prev_princess_index)
            upper_bound = calculate_princess_upper_bound(prev_lower_bound, copy_value_arr, cell_title_arr,
                                                         dragon_count(dragons_in_range_title), i, prev_princess_index)
            # if lower bound is insufficient - return empty bound (this condition may be unnecessary)
            if len(lower_bound) < copy_value_arr[i]:
                return [], []
            else:
                # return bounds
                return lower_bound, upper_bound
    return [], []


'''
output_array - this array contains the lower_bound and upper_bound for each princess
value_array - cell_value_arr (input)
n - index of princess we want to print
this function prints the output according to the instruction
'''


def print_result(output_array, value_array, n):
    if len(output_array[n][0]) == 0:
        print(-1)
    else:
        indices_arr = output_array[n][1].astype(int)
        maximum_num_of_coins = value_array[indices_arr].sum()
        num_of_dragons_to_kill = len(output_array[n][1])
        cells_ascending = np.sort(output_array[n][1]).astype(int) + 1
        print(int(maximum_num_of_coins))
        print(num_of_dragons_to_kill)
        for i in cells_ascending:
            print(i, end=" ")


'''
title_arr - cell_title_arr (input)
value_array - cell_value_arr (input)
this function initializes output_array, fills it and prints it
'''


def run(title_arr, value_arr):
    output_arr = [[] for i in range(len(title_arr))]
    for i in range(len(title_arr)):
        output_arr[i] = max_coins_per_index(i, title_arr, value_arr, output_arr)
    print_result(output_arr, value_arr, len(output_arr) - 1)


'''
this parses the input and runs run()
'''


def main():
    title_arr, value_arr = parse_input_file("input_file.yaml")
    if len(title_arr) != 0:
        run(title_arr, value_arr)


main()
