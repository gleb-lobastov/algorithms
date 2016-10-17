import random


def quick_sort3(arr):
    """ Implementation of QuickSort3 algorithm. Sort array in place """
    _quick_sort3(arr)


def _quick_sort3(arr, l=0, r=None):
    if r is None:
        r = len(arr)

    while r - l > 1:
        pivot_idx = random.randint(l, r - 1)
        pivot = arr[pivot_idx]
        j = k = l
        for i in range(l, r):
            # This node is preliminary, where designated starting cell and pivot value is placed inside
            if pivot_idx is not None:
                if arr[i] < pivot:
                    # Skip all first elements which is less that pivot value
                    continue
                elif arr[i] > pivot:
                    arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
                    j = k = i
                else:
                    # There current element is pivot value
                    j = i - 1
                    k = i
                pivot_idx = None

            # Main sorting loop
            else:
                # j points to last element which is less than pivot value, k to last equal element
                less = arr[i] < pivot
                if arr[i] <= pivot:
                    k += 1
                    if i != k:
                        arr[i], arr[k] = arr[k], arr[i]

                if less:
                    j += 1
                    if i != j:
                        arr[k], arr[j] = arr[j], arr[k]

        if j - l >= 1:
            _quick_sort3(arr, l, j + 1)
        l = k + 1


def test():
    import timeit

    def test_quick_sort3(arr):
        quick_sort3(arr)
        return arr

    assert test_quick_sort3([1, 2, 3]) == [1, 2, 3]
    assert test_quick_sort3([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert test_quick_sort3([1, 3, 3, 4]) == [1, 3, 3, 4]
    assert test_quick_sort3([1, 3, 2, 4]) == [1, 2, 3, 4]
    assert test_quick_sort3([1, 3, 4, 2]) == [1, 2, 3, 4]
    assert test_quick_sort3([1, 4, 3, 2]) == [1, 2, 3, 4]
    assert test_quick_sort3([2, 3, 9, 2, 9]) == [2, 2, 3, 9, 9]
    assert test_quick_sort3([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # testing large array with random data
    array = [random.randint(0, 10**9) for _ in range(10**5)]
    sorted_array = list(sorted(array))

    timing = timeit.timeit(lambda: quick_sort3(array), number=1)
    assert timing < 3
    assert array == sorted_array

    # testing large array with a lot of repeating of several different values
    array = [random.randint(0, 100) for _ in range(10**5)]
    sorted_array = list(sorted(array))

    timing = timeit.timeit(lambda: quick_sort3(array), number=1)
    assert timing < 3
    assert array == sorted_array

    print('tests passed')


if __name__ == "__main__":
    test()
