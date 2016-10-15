"""
Первая строка содержит число 1≤n≤10^5, вторая — массив A[1…n], содержащий натуральные числа,
не превосходящие 10^9. Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
(Такая пара элементов называется инверсией массива. Количество инверсий в массиве является
в некотором смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве
инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
"""

TESTING = False


def count_inversions(array):
    """ Count array inversions during sorting (count of A[i]>A[j] for each i, j of 1≤i<j≤n) """
    def merge(lo, hi):
        nonlocal inversions
        # reversing to use pop method instead of recreating list by slicing
        lo.reverse()
        hi.reverse()
        l, h = None, None
        while lo or hi or l or h:
            l = lo.pop() if lo and l is None else l
            h = hi.pop() if hi and h is None else h
            if h is None or (l is not None and l <= h):
                yield l
                l = None
            else:
                if l is not None:
                    # In ordered list items in right (hi) part will be greater than items in left (lo) part.
                    # Reaching this point mean that this rule is violated for each item of lo include
                    # popped one. So it's equivalent to len(lo) + 1 inversions, which is accounted here
                    inversions += len(lo) + 1
                yield h
                h = None

    inversions = 0

    # current and further variables is used to separate each round of array circumvention
    # what is necessary to retain relative order of items until direct comparison, where
    # is possible to admit shifting and increase inversion count
    current = list(map(lambda i: [i], array))
    further = []
    while len(current) > 1:

        # reversing to use pop method instead of recreating list by slicing
        current.reverse()
        while len(current) > 1:
            further.append(list(merge(current.pop(), current.pop())))

        # consider odd item
        if current:
            further.append(current.pop())
        current, further = further, []
    return inversions


def main():
    _ = input()
    array = map(int, input().split())
    print(count_inversions(array))


def test():
    assert count_inversions([1, 2, 3]) == 0
    assert count_inversions([1, 2, 3, 4]) == 0
    assert count_inversions([1, 3, 3, 4]) == 0
    assert count_inversions([1, 3, 2, 4]) == 1
    assert count_inversions([1, 3, 4, 2]) == 2
    assert count_inversions([1, 4, 3, 2]) == 3
    assert count_inversions([2, 3, 9, 2, 9]) == 2
    assert count_inversions([5, 4, 3, 2, 1]) == 10

    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
