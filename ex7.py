#################################################################
# FILE : ex7.py
# WRITER : Geva Haviv
# DESCRIPTION:
# WEB PAGES I USED:
# NOTES:
#################################################################

import ex7_helper
import typing


# ---------------------------- PART 1 ----------------------------


def mult(x: float, y: int) -> float:
    """
    This function mult x by y in runtime O(n).
    x = float number.
    y = int number.
    Input: x, y.
    Output: float.
    """

    if y == 0 or x == 0:
        return 0
    if y == 1:
        return x

    return ex7_helper.add(mult(x, ex7_helper.subtract_1(y)), x)


def is_even(n: int) -> bool:
    """
    This function check if the number is even in runtime O(n).
    x = int number.
    Input: x.
    Output: Bool.
    """

    if n == 0:
        return True
    elif n < 0:
        return False

    return is_even(ex7_helper.subtract_1(ex7_helper.subtract_1(n)))


def log_mult(x: float, y: int) -> float:
    """
    This function mult x by y in runtime O(log n).
    x = float number.
    y = int number.
    Input: x, y.
    Output: float.
    """

    if y == 0:
        return 0
    if y == 1:
        return x

    if ex7_helper.is_odd(y):
        return ex7_helper.add(log_mult(ex7_helper.add(x, x), ex7_helper.divide_by_2(y)), x)
    return log_mult(ex7_helper.add(x, x), ex7_helper.divide_by_2(y))


def _is_power_helper(b: int, n: int, x: int) -> int:
    """
    This function multiple the number b by b until we got number >= x,
    the runtime is O(log(b) * log(x)).
    b = the number we multiple by the base, type int.
    n = base number, type int.
    x = the number we try to reach, type int.
    Input: b, n, x.
    Output: int.
    """

    if b == 1:
        return 1
    if b >= x:
        return b

    return _is_power_helper(int(log_mult(b, n)), n, x)


def is_power(b: int, x: int) -> bool:
    """
    This function check if there is some n that the number b^n = x,
    the runtime is O(log(b) * log(x)).
    b = int number.
    x = int number.
    Input: b, x.
    Output: Bool.
    """
    if b == 0:
        return x == 0
    if x == 1:
        return True
    b = _is_power_helper(b, b, x)

    return b == x


def _reverse_helper(s: str, index: int, reversed_text: str) -> str:
    """
    This function take each time the last char from s and put it in first index in reversed_text.
    the runtime is O(log len(s)).
    s = text, type string.
    index = index from the last char of s, type int.
    text = the reversed_text, type string.
    Input: s, index, text.
    Output: string.
    """

    if index == -1:
        return reversed_text

    return _reverse_helper(s, index - 1, ex7_helper.append_to_end(reversed_text, s[index]))


def reverse(s: str) -> str:
    """
    This function returned the reversed text of s,
    the runtime is O(log len(s)).
    s = text, type sting.
    Input: s.
    Output: string.
    """

    return _reverse_helper(s, len(s) - 1, '')


# ---------------------------- PART 2 ----------------------------


def play_hanoi(hanoi: typing.Any, n: int, src: typing.Any, dst: typing.Any, temp: typing.Any) -> None:
    """
    This function run the hanoi game, the runtime is O(log n).
    hanoi = object, type any.
    n = number of disk, type int.
    src = object that represents the first rod, type any.
    dst = object that represents the last rod, type any.
    temp = object that represents the middle rod, type any.
    Input: hanoi, n, src, dst, temp.
    Output: None.
    """

    if n < 0:
        n = 0

    if n > 0:
        play_hanoi(hanoi, n - 1, src, temp, dst)

        hanoi.move(src, dst)

        play_hanoi(hanoi, n - 1, temp, dst, src)


def _count_ones_in_number(n: int, count: int) -> int:
    """
    This function count the number of ones in number n,
    the runtime is O(log n).
    n = number, type int.
    count = number, type int.
    Input: n, count.
    Output: int.
    """

    if n == 0:
        return count
    if n % 10 == 1:
        return _count_ones_in_number(n // 10, count + 1)

    return _count_ones_in_number(n // 10, count)


def _number_of_ones_helper(n: int, s: int) -> int:
    """
    This function sum all the ones in all the number from 1 to n,
    the runtime is O(log n).
    n = number, type int.
    s = sum, type int.
    Input: n, s.
    Output: int.
    """

    if n == 0:
        return s

    s += _count_ones_in_number(n, 0)
    return _number_of_ones_helper(n - 1, s)


def number_of_ones(n: int) -> int:
    """
    This function return the number of ones in all the numbers from 1 to n,
    the runtime is O(log n).
    n = number, type int.
    Input: n.
    Output: int.
    """

    return _number_of_ones_helper(n, 0)


def _helper_compare_1d_lists(l1: list[int], l2: list[int], index: int) -> bool:
    """
    This function check if the lists are equal,
    the runtime is O(len(l1)).
    l1 = list, type list.
    l2 = list, type list.
    index = index of lst, type int.
    Input: l1 ,l2, index.
    Output: Bool.
    """

    if len(l1) == 0 and len(l2) == 0:
        return True
    if len(l1) != len(l2) or l1[index] != l2[index]:
        return False
    if index == len(l1) - 1:
        return True

    return _helper_compare_1d_lists(l1, l2, int(ex7_helper.add(index, 1)))


def _helper_compare_2d_lists(l1: list[list[int]], l2: list[list[int]], index: int) -> bool:
    """
    This function return True if the lists are equal and False otherwise,
    the runtime is O(len(l1) * len(l1[index])).
    l1 = list, type list.
    l2 = list, type list.
    index = index of lst, type int.
    Input: l1 ,l2, index.
    Output: Bool.
    """

    if not _helper_compare_1d_lists(l1[index], l2[index], 0):
        return False
    if index == len(l1) - 1:
        return True

    return _helper_compare_2d_lists(l1, l2, int(ex7_helper.add(index, 1)))


def compare_2d_lists(l1: list[list[int]], l2: list[list[int]]) -> bool:
    """
    This function return True if the lists are equal and False otherwise,
    the runtime is O(len(l1) * len(l1[index])).
    l1 = list, type list.
    l2 = list, type list.
    Input: l1 ,l2.
    Output: Bool.
    """

    if len(l1) != len(l2):
        return False
    if len(l1) == 0 and len(l2) == 0:
        return True

    return _helper_compare_2d_lists(l1, l2, 0)


def magic_list(n: int) -> list[typing.Any]:
    """
    This function return list from type(Any),
    the runtime is O(n).
    n = the length of the list
    Input: n.
    Output: list[Any].
    """

    if n == 0:
        return []

    lst = magic_list(n - 1)
    lst.append(magic_list(n - 1))

    return lst
