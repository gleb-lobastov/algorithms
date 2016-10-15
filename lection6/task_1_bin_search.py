"""
В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных натуральных чисел, не превышающих 10^9,
в порядке возрастания, во второй — целое число 1≤k≤10^5 и k натуральных чисел b1,…,bk, не превышающих 10^9.
Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=b_i, или −1, если такого j нет.
"""
import math

TESTING = False


def find(sorted_array, key):
    left_bound, right_bound = 0, len(sorted_array)
    while left_bound < right_bound:
        middle = right_bound - math.ceil((right_bound - left_bound) / 2)
        if sorted_array[middle] == key:
            return middle + 1
        elif sorted_array[middle] < key:
            left_bound = middle + (1 if left_bound == middle else 0)
        else:
            right_bound = middle
    return -1


def main():
    _, *sorted_array = map(int, input().split())
    _, *keys = map(int, input().split())
    print(' '.join(str(find(sorted_array, key)) for key in keys))


def test():
    assert find([], 1) == -1
    assert find([10], 0) == -1
    assert find([10], 10) == 0
    assert find([10], 20) == -1
    assert find([10, 20], 0) == -1
    assert find([10, 20], 10) == 0
    assert find([10, 20], 20) == 1
    assert find([10, 20], 30) == -1
    assert find([11, 22, 33, 44, 55, 66, 77, 88, 99], 11) == 0
    assert find([11, 22, 33, 44, 55, 66, 77, 88, 99], 44) == 3
    assert find([11, 22, 33, 44, 55, 66, 77, 88, 99], 99) == 8
    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
