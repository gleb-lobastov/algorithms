"""
Дано целое число 1≤n≤10^5и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие
10^9. Найдите наибольшую невозрастающую подпоследовательность в A. В первой строке выведите её
длину k, во второй — её индексы 1≤i1<i2<…<ik≤n (таким образом, A[i1]≥A[i2]≥…≥A[in]).

Given an integer 1≤n≤10^5 and array a[1...n] contains the non-negative integers not exceeding
10^9. Find greatest non-increasing subsequence in A. In the first line print it
the length of k, the second, the indexes 1≤i1<i2<...<ik≤n (thus, A[i1]≥A[i2]≥...≥A[in]).
"""

TESTING = False


def bisect_right_desc(desc_list, value):
    """ bisect.bisect equivalent for descending sequences """
    lo = 0
    hi = len(desc_list)

    while lo < hi:
        mid = (lo + hi) // 2
        if value > desc_list[mid]:
            hi = mid
        else:
            lo = mid + 1

    return lo


def longest_non_inc_subseq(sequence):
    """ Lookup for longest non-increasing subsequence in given sequence """

    # Values to calculate
    longest_subseq_length = 0
    longest_subseq_indices = []

    # Longest subseq lengths. Share index with sequence
    longest_subseq_lengths = []

    # List of sequence greatest values for each possible length of subseq.
    # The joke is that values will also be sorted in descending order.
    highs = []

    for value in sequence:

        # Lookup for subseq length of value
        subseq_length = bisect_right_desc(highs, value)

        if subseq_length >= longest_subseq_length:

            # If we found new subseq maximum, then just append it to highs
            highs.append(value)
            longest_subseq_length += 1
        else:

            # If value already present in highs, then lookup returns subseq length
            # that correspond for previous item of sequence with same value.
            # Thus we should increase it.
            if highs[subseq_length] == value:
                subseq_length += 1

            # Otherwise, if value is not present, lookup will return appropriate subseq length
            highs[subseq_length] = value
        longest_subseq_lengths.append(subseq_length)

    # Counter for restoring. It starting from discovered subseq length, given the fact that
    # resulting subsequence is by one greater than greatest subsequence found for item,
    # because it contains that item.
    current_high = longest_subseq_length - 1

    # Restore subsequence indices
    for index, subseq_length in reversed(list(enumerate(longest_subseq_lengths))):
        if subseq_length == current_high:
            longest_subseq_indices.append(index)
            current_high -= 1

    # Arrange output in order of appearance in the sequence
    longest_subseq_indices.reverse()

    return longest_subseq_length, longest_subseq_indices


def main():
    _ = input()
    sequence = list(map(int, input().split()))
    longest_subseq_length, longest_subseq_indices = longest_non_inc_subseq(sequence)
    print(longest_subseq_length)
    print(' '.join(str(index + 1) for index in longest_subseq_indices))


def test():
    import timeit
    import random

    def test_sequence(sequence, expected_length):
        length, subsequence_indices = longest_non_inc_subseq(sequence)
        assert len(subsequence_indices) == length
        if expected_length != -1:
            assert length == expected_length
        for index in range(1, len(subsequence_indices)):
            assert subsequence_indices[index] > subsequence_indices[index - 1]
            assert sequence[subsequence_indices[index]] <= sequence[subsequence_indices[index - 1]]

    test_sequence([], 0)
    test_sequence([1], 1)
    test_sequence([3, 2, 1], 3)
    test_sequence([2, 2, 2], 3)
    test_sequence([1, 2, 1], 2)
    test_sequence([1, 2, 2], 2)
    test_sequence([1, 2, 3], 1)
    test_sequence([2, 10, 2, 11, 2, 12, 2], 4)
    test_sequence([7, 6, 5, 6, 8, 4, 5, 5, 6, 7, 3, 4], 6)
    test_sequence([5, 3, 4, 4, 2], 4)

    long_sequence = list(random.randint(1, 1000000000) for _ in range(10000))
    test_sequence(long_sequence, -1)

    timing = timeit.timeit(lambda: longest_non_inc_subseq(long_sequence), number=1)
    print(timing)
    assert timing < 5

    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
