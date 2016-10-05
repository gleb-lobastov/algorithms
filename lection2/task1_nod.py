def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    # main()
    assert gcd(18, 35) == 1
    assert gcd(14159572, 63967072) == 4
    assert gcd(144, 96) == 48
    print('tests passed')
