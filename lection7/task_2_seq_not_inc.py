"""
Дано целое число 1≤n≤10^5и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие
10^9. Найдите наибольшую невозрастающую подпоследовательность в A. В первой строке выведите её
длину k, во второй — её индексы 1≤i1<i2<…<ik≤n (таким образом, A[i1]≥A[i2]≥…≥A[in]).

Given an integer 1≤n≤10^5 and array a[1...n] contains the non-negative integers not exceeding
10^9. Find greatest non-increasing subsequence in A. In the first line print it
the length of k, the second, the indexes 1≤i1<i2<...<ik≤n (thus, A[i1]≥A[i2]≥...≥A[in]).
"""
TESTING = True


def non_inc_subsequence(sequence):
    length = len(sequence)
    subseq_lengths = [1] * length
    for i in range(length):
        for j in range(i):
            if sequence[i] <= sequence[j] and subseq_lengths[j] + 1 > subseq_lengths[i]:
                subseq_lengths[i] = subseq_lengths[j] + 1

    longest_subseq_length = max(subseq_lengths)
    longest_subseq_indices = []

    last_index = length
    for seq_len in range(longest_subseq_length, 0, -1):
        _, last_index = max(
            (sequence[subseq_index], subseq_index)
            for subseq_index, subseq_length in enumerate(subseq_lengths[:last_index])
            if subseq_length == seq_len
        )
        longest_subseq_indices.append(last_index)

    longest_subseq_indices.reverse()
    return longest_subseq_length, longest_subseq_indices


def main():
    _ = input()
    sequence = list(map(int, input().split()))
    longest_subseq_length, longest_subseq_indices = non_inc_subsequence(sequence)
    print(longest_subseq_length)
    print(' '.join(str(index + 1) for index in longest_subseq_indices))


def test():
    import timeit
    import random

    fail = False

    def test_sequence(sequence, expected_length):
        nonlocal fail
        length, subsequence_indices = non_inc_subsequence(sequence)
        try:
            if expected_length >= 0:
                assert len(subsequence_indices) == expected_length == length
            for index in range(1, len(subsequence_indices)):
                assert subsequence_indices[index] > subsequence_indices[index - 1]
                assert sequence[subsequence_indices[index]] <= sequence[subsequence_indices[index - 1]]
        except AssertionError:
            fail = True

    test_sequence([3, 2, 1], 3)
    test_sequence([2, 2, 2], 3)
    test_sequence([1, 2, 1], 2)
    test_sequence([1, 2, 2], 2)
    test_sequence([1, 2, 3], 1)
    test_sequence([2, 10, 2, 11, 2, 12, 2], 4)
    test_sequence([5, 3, 4, 4, 2], 4)

    long_sequence = list(random.randint(1, 1000000000) for _ in range(10000))
    test_sequence(long_sequence, -1)
    assert not fail

    timing = timeit.timeit(lambda: non_inc_subsequence(long_sequence), number=1)
    print(timing)
    assert timing < 5

    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
