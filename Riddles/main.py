import math
import itertools
# without temporary variable
import random
import sys
from collections import Counter


def switch_a_b_value(a, b):
    a, b = b, a
    return a, b


def is_flat(lst):
    if type(lst) is not list:
        return True
    for l in lst:
        if type(l) is list:
            return False
    return True


global_lst = []


# Given a list of lists - flattens the list into a list of non list objects
# using recursion and a global variable


def flat_list_of_lists(list_of_lists) -> object:
    if is_flat(list_of_lists):
        if type(list_of_lists) is not list:
            global_lst.append(list_of_lists)
        else:
            for e in list_of_lists:
                global_lst.append(e)
        return None
    for i in range(len(list_of_lists)):
        flat_list_of_lists(list_of_lists[i])
    return None


def fetch_every_third_item_1(lst):
    ret = []
    for i in range(0, len(lst), 3):
        ret.append(lst[i])

    return ret


def fetch_every_third_item_2(lst):
    for i in range(0, len(lst), 3):
        yield lst[i]


def fetch_every_third_item_3(lst):
    ret = []
    for i in range(len(lst)):
        if i % 3 == 0:
            ret.append(lst[i])
    return ret


# This function removes duplicate consecutive characters form str1
def remove_duplicate_consecutive_char(str1):
    ret = ""
    i = 0
    while i < len(str1):
        ret += str1[i]
        j = i + 1
        while j < len(str1) and str1[i] == str1[j]:
            j += 1
            i += 1
        i += 1

    return ret


# This function gets random indices i,j in the board and and color (color is a number)
# and like the fill function in Paint it colors the board
# we use the function print_board to print

def spread_from_given_index(board, i, j, color):
    if i >= len(board):
        return
    if j >= len(board[0]):
        return
    if board[i][j] != 0:
        return
    board[i][j] = color
    spread_from_given_index(board, i + 1, j, color)
    spread_from_given_index(board, i, j + 1, color)
    spread_from_given_index(board, i - 1, j, color)
    spread_from_given_index(board, i, j - 1, color)
    return board


def print_board(board):
    for line in board:
        print(line)


# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list
# Assume lent(lst2)>= len(lst1)
def add_two_numbers(lst1, lst2):
    ret = []
    i, j = 0, 0
    memory = 0
    for i in range(len(lst1)):
        digit = lst2[i] + lst1[i] + memory
        memory = 0
        if digit > 9:
            memory = 1
        ret.append(digit % 10)
    j = i + 1

    while j < len(lst2):
        digit = lst2[j] + memory
        memory = 0
        if digit > 9:
            memory = 1
        ret.append(digit % 10)
        j += 1

    if memory == 1:
        ret.append(1)

    return ret


# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

# def median_of_two_sorted_arrays(arr1, arr2):
#     n = len(arr1)
#     m = len(arr2)
#     while n > 2 or m > 2:
#         median1 = arr1[int(math.ceil(n / 2) - 1)]
#         median2 = arr2[int(math.ceil(m / 2) - 1)]
#         if median1 < median2:
#             arr2 = arr2[:int(math.ceil(m / 2))]
#             arr1 = arr1[int(math.ceil(n / 2) - 1):]
#         else:
#             arr1 = arr1[:int(math.ceil(n / 2))]
#             arr2 = arr2[int(math.ceil(m / 2) - 1):]
#         n = len(arr1)
#         m = len(arr2)
#
#     if n == m == 1:
#         return min(arr1[0], arr2[0])
#     elif n == m == 2:
#         return max(min(arr1[0], arr2[1]), min(arr1[1], arr2[0]))
#     elif n == 1:
#         return min(arr1[0], arr2[1])
#     else:
#         return min(arr1[1], arr2[0])

def get_palindrome_length_around_index(str1, left_index, right_index):
    while left_index >= 0 and right_index < len(str1) and str1[left_index] == str1[right_index]:
        left_index -= 1
        right_index += 1
    return right_index - left_index - 1


# Given a string s, return the longest palindromic substring in s.
def find_longest_palindrome(str1):
    start_index, end_index = 0, 0
    for i in range(len(str1)):
        palindrome_len1 = get_palindrome_length_around_index(str1, i, i)
        palindrome_len2 = get_palindrome_length_around_index(str1, i, i + 1)
        max_len = max(palindrome_len1, palindrome_len2)
        if max_len > end_index - start_index:
            start_index = i - int((max_len - 1) / 2)
            end_index = i + int(max_len / 2)
    return str1[start_index:end_index + 1]


def get_second_largest_value(arr):
    # There is no second largest value
    if len(arr) < 2:
        return None
    minimal_int_val = -sys.maxsize - 1
    first, second = minimal_int_val, minimal_int_val

    for i in range(len(arr)):
        if arr[i] > first:
            # Now first is the maximum, and second is next to maximum
            second = first
            first = arr[i]

        # If arr[i] is in between first and second then only second should be updated
        elif first > arr[i] > second:
            second = arr[i]

    # There is no second largest value
    if second == minimal_int_val:
        return None
    else:
        return second


def char_counter(s):
    count = 0
    for i in range(len(s)):
        if str(s[i]).isalpha():
            count += 1
    return count


def digit_counter(s):
    count = 0
    for i in range(len(s)):
        if str(s[i]).isdigit():
            count += 1
    return count


# it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
# there should be an even number of letters;
# there should be an odd number of digits.
def is_valid_password(password):
    return str(password).isalnum() and digit_counter(password) % 2 == 1 \
           and char_counter(password) % 2 == 0


# that, given a non-empty string S consisting of N characters, returns the length of the longest word from the string
# that is a valid password.
def get_longest_password(s):
    possible_pass = str(s).split()
    longest_password = ''
    for password in possible_pass:
        if is_valid_password(password) and len(password) > len(longest_password):
            longest_password = password
    if longest_password != '':
        return longest_password
    return None


def unique_permutation(nums):
    results = []

    def backtrack(comb, counter):
        if len(comb) == len(nums):
            # make a deep copy of the resulting permutation,
            # since the permutation would be backtracked later.
            results.append(list(comb))
            return

        for num in counter:
            if counter[num] > 0:
                # add this number into the current combination
                comb.append(num)
                counter[num] -= 1
                # continue the exploration
                backtrack(comb, counter)
                # revert the choice for the next exploration
                comb.pop()
                counter[num] += 1

    backtrack([], Counter(nums))

    return results


def all_permutation(nums):
    return list(itertools.permutations(nums))


import itertools
class Solution(object):
    def permuteUnique(self, nums):
        results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results