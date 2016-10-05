"""
Дано число 1 ≤ n ≤ 10^7, необходимо найти последнюю цифру n-го числа Фибоначчи.
"""


def fib_digit(n):
    last_pair = 0, 1

    if n in last_pair:
        return n

    for _ in range(n - 1):
        last_pair = last_pair[1], sum(last_pair) % 10

    return last_pair[1]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    # main()

    assert fib_digit(0) == 0
    assert fib_digit(1) == 1
    assert fib_digit(2) == 1
    assert fib_digit(10) == 5
    assert fib_digit(193150) == 5
    print('tests passed')
