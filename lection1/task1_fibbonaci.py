"""
Дано целое число 1≤ n ≤40, необходимо вычислить n-е число Фибоначчи
F0 = 0, F1 = 1
"""


def fib(n):
    last_pair = 0, 1

    if n in last_pair:
        return n

    for _ in range(n - 1):
        last_pair = last_pair[1], sum(last_pair)

    return last_pair[1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(10) == 55
    assert fib(40) == 102334155
    print('tests passed')
