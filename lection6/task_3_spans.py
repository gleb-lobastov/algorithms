"""
В первой строке задано два целых числа 1≤n≤50000 — количество отрезков и точек на прямой, соответственно.
Следующие n строк содержат по два целых числа a_i и b_i (a_i≤b_i) — координаты концов отрезков.
Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе. Для каждой точки в
порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""

import math
from lection6.quick_sort3 import quick_sort3

TESTING = False


def sort(arr):
    arr = list(arr)
    quick_sort3(arr)
    return arr


def bisect(sorted_array, key, lookup_rightmost):
    left_bound, middle, right_bound = 0, 0, len(sorted_array)

    if sorted_array[0] > key:
        return 0
    if sorted_array[right_bound - 1] < key:
        return right_bound

    while left_bound < right_bound:
        middle = right_bound - math.ceil((right_bound - left_bound) / 2)
        if sorted_array[middle] == key:
            if lookup_rightmost and middle != right_bound - 1:
                left_bound = middle
            elif not lookup_rightmost and middle != left_bound:
                right_bound = middle
            else:
                return middle + (1 if lookup_rightmost else 0)
        elif sorted_array[middle] < key:
            left_bound = middle + (1 if left_bound == middle else 0)
        else:
            right_bound = middle
    return left_bound


def spans_contain_point_count(spans, points):
    spans_starts, spans_ends = map(sort, zip(*spans))
    return list(bisect(spans_starts, point, True) - bisect(spans_ends, point, False) for point in points)


def main():
    spans_count, _ = map(int, input().split())
    spans = list(map(int, input().split()) for _ in range(spans_count))
    points = tuple(map(int, input().split()))
    print(*spans_contain_point_count(spans, points), sep=' ')


def test():
    import timeit
    import random

    assert spans_contain_point_count([(0, 5), (7, 10)], (1, 6, 11)) == [1, 0, 0]
    assert spans_contain_point_count([(0, 7), (5, 10)], (7, 5, 6)) == [2, 2, 2]
    assert spans_contain_point_count([(0, 3), (3, 5)], (2, 3, 4)) == [1, 2, 1]
    assert spans_contain_point_count([(0, 3), (3, 3), (3, 5)], (2, 3, 4)) == [1, 3, 1]
    assert spans_contain_point_count(
        [(1, 10), (3, 8), (5, 6)],
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    ) == [0, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 0]

    spans = []
    points = []
    for _ in range(50000):
        x = random.randint(1, 10**8 - 1)
        y = random.randint(x, 10**8)
        spans.append((x, y))
        points.append(random.randint(1, 10**8))

    timing = timeit.timeit(lambda: spans_contain_point_count(spans, points), number=1)
    assert timing < 3

    spans = []
    points = []
    for _ in range(50000):
        x = random.randint(1, 999)
        y = random.randint(x, 1000)
        spans.append((x, y))
        points.append(random.randint(1, 1000))

    timing = timeit.timeit(lambda: spans_contain_point_count(spans, points), number=1)
    assert timing < 3

    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
