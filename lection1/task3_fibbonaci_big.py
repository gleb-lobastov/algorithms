"""
Даны целые числа 1 ≤ n ≤ 10^18 и 2 ≤ m ≤ 10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.
"""


def fib(n):
    last_pair = 0, 1

    if n in last_pair:
        return n

    for _ in range(n - 1):
        last_pair = last_pair[1], sum(last_pair)

    return last_pair[1]


def pisano(m):
    """ Возвращает период Пизано — переид повтора последних цифр для чисел Фиббоначи взятых по модулю m """
    # Начинаем со второго шага, что-бы сразу не было выполнено условие выхода из цикла
    counter = 1  # вместо 0
    last_pair = 1, 1  # вместо 0, 1

    while last_pair != (0, 1):
        counter += 1
        last_pair = last_pair[1], sum(last_pair) % m

    return counter


def fib_mod(n, m):
    """ Решает задачу с учетом периода повтора последних цифр """
    return fib(n % pisano(m)) % m


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
    assert fib_mod(1, 2) == 1
    assert fib_mod(10, 2) == 1
    assert fib_mod(150000, 100000) == 0
    assert fib_mod(372718000010, 2) == 1
    assert fib_mod(1000000000001, 99999) == 63715
    assert fib_mod(100000000000000000000000000001, 100) == 1
    print('tests passed')
