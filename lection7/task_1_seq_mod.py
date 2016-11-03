"""
Дано целое число 1≤n≤10^3 и массив A[1…n]  натуральных чисел, не превосходящих 2⋅109^9.
Выведите максимальное 1≤k≤n, для которого найдётся подпоследовательность 1≤i1<i2<…<ik≤n
длины k, в которой каждый элемент делится на предыдущий (формально: для  всех 1≤j<k, A[ij]|A[ij+1]).

Given an integer 1≤n≤10^3 and array a[1...n] of positive integers, not exceeding 2⋅109^9.
Output the maximum 1≤k≤n, for which there is a subsequence 1≤i1<i2<...<ik≤n
of length k in which each element is divided by the previous (formally: for all 1≤j<k, A[ij]|A[ij+1]).
"""
TESTING = False


def divisible_subsequence(sequence):
    length = len(sequence)
    max_subsequences = [1] * length
    for i in range(length):
        for j in range(i):
            if not(sequence[i] % sequence[j]) and max_subsequences[j] + 1 > max_subsequences[i]:
                max_subsequences[i] = max_subsequences[j] + 1
    return max(max_subsequences)


def main():
    _ = input()
    sequence = list(map(int, input().split()))
    print(divisible_subsequence(sequence))


def test():
    assert divisible_subsequence([1]) == 1
    assert divisible_subsequence([2, 3]) == 1
    assert divisible_subsequence([2, 4]) == 2
    assert divisible_subsequence([2, 4, 5]) == 2
    assert divisible_subsequence([2, 4, 6]) == 2
    assert divisible_subsequence([2, 4, 8]) == 3
    assert divisible_subsequence([2, 4, 8, 9]) == 3
    assert divisible_subsequence([2, 4, 8, 9, 12, 15, 32]) == 4
    assert divisible_subsequence([3, 6, 7, 12]) == 3
    assert divisible_subsequence([1, 1, 1, 1]) == 4
    assert divisible_subsequence([1, 2, 3, 5, 9, 5, 18]) == 4
    assert divisible_subsequence([1, 2, 3, 4, 9, 8, 18, 16]) == 5

    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
