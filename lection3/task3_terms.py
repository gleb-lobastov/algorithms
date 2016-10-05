"""
По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n можно представить
как сумму k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.
"""
TESTING = False


def decompose(number):
    term = 1
    terms = []
    while number:
        if term > number:
            terms[-1] += number
            return terms
        terms.append(term)
        number -= term
        term += 1
    return terms


def main():
    number = int(input())
    assert number > 0
    terms = decompose(number)
    print(len(terms))
    print(*terms, sep=' ')


def test():
    print(*((x, decompose(x)) for x in range(1, 20)))
    assert decompose(1) == [1]
    assert decompose(2) == [2]
    assert len(decompose(4)) == 2
    assert len(decompose(6)) == 3
    assert len(decompose(7)) == 3
    assert len(decompose(17)) == 5
    assert all(arg == sum(decompose(arg)) for arg in [1, 2, 4, 8, 16, 32])
    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
