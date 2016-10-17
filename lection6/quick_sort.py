def quick_sort(array):
    """ Implementation of QuickSort algorithm. Sort array in place """
    _quick_sort(array)


def _quick_sort(array, l=0, r=None):
    if r is None:
        r = len(array)

    if r - l <= 1:
        return

    inv = array[l]
    j = l
    for i in range(l + 1, r):
        if array[i] < inv:
            j += 1
            if i != j:
                array[i], array[j] = array[j], array[i]
    if l != j:
        array[l], array[j] = array[j], inv

    _quick_sort(array, l, j)
    _quick_sort(array, j + 1, r)


def test():
    import timeit
    import random

    def test_quick_sort(arr):
        quick_sort(arr)
        return arr

    assert test_quick_sort([1, 2, 3]) == [1, 2, 3]
    assert test_quick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert test_quick_sort([1, 3, 3, 4]) == [1, 3, 3, 4]
    assert test_quick_sort([1, 3, 2, 4]) == [1, 2, 3, 4]
    assert test_quick_sort([1, 3, 4, 2]) == [1, 2, 3, 4]
    assert test_quick_sort([1, 4, 3, 2]) == [1, 2, 3, 4]
    assert test_quick_sort([2, 3, 9, 2, 9]) == [2, 2, 3, 9, 9]
    assert test_quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    array = [random.randint(0, 10**9) for _ in range(10**5)]
    sorted_array = list(sorted(array))

    timing = timeit.timeit(lambda: quick_sort(array), number=1)
    assert timing < 3
    assert array == sorted_array

    print('tests passed')


if __name__ == "__main__":
    test()
