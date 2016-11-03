"""
The first line contains an integer 1≤n≤10^4, the second n integers not exceeding 10.
Print ordered by non-decreasing sequence of these numbers.

Первая строка содержит число 1≤n≤10^4, вторая — n натуральных чисел, не превышающих 10.
Выведите упорядоченную по неубыванию последовательность этих чисел.
"""
import math

TESTING = False

NUMBER_SYSTEM = 10


def get_digit(number, position=0):
    return number // 10**position % 10


def non_comparison_sort_by_digit(array, position):
    slots = [0] * NUMBER_SYSTEM
    for number in array:
        slots[get_digit(number, position)] += 1

    for index in range(1, len(slots)):
        slots[index] += slots[index - 1]

    result = [0] * len(array)
    for item in reversed(array):
        digit = get_digit(item, position)
        result[slots[digit] - 1] = item
        slots[digit] -= 1

    return result


def non_comparison_sort(array, max_digits=None):
    if max_digits is None:
        max_digits = int(math.log(max(array), NUMBER_SYSTEM)) + 1

    for digit in range(max_digits):
        array = non_comparison_sort_by_digit(array, digit)

    return array


def main():
    _ = input()
    array = list(map(int, input().split()))
    print(' '.join(map(str, non_comparison_sort(array))))


def test():
    import timeit
    import random

    def is_correct(items, max_digits=None):
        return non_comparison_sort(items, max_digits) == list(sorted(items))

    assert get_digit(0) == 0
    assert get_digit(345) == 5
    assert get_digit(0, 1) == 0
    assert get_digit(345, 1) == 4
    assert get_digit(345, 2) == 3
    assert is_correct([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert is_correct([9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert is_correct([3, 2, 1, 3, 2, 1, 3, 2, 1])
    assert is_correct([3, 1, 2, 4, 5, 1, 2, 3, 4])
    assert is_correct([1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert is_correct([333, 333, 222, 222, 111, 111])
    assert is_correct([321, 312, 231, 213, 132, 123])
    assert is_correct([321, 312, 231, 213, 132, 123])
    assert is_correct([222, 221, 212, 211, 122, 121, 112, 111])
    assert is_correct([222, 221, 212, 211, 122, 121, 112, 111], 3)
    assert is_correct([1, 9, 2, 8, 3, 7, 10, 10, 10])

    random_array = [random.randint(1, 999) for _ in range(10000)]
    assert is_correct(random_array)

    timing = timeit.timeit(lambda: non_comparison_sort(random_array, 3), number=1)
    assert timing < 3

    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
