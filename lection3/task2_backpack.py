"""
Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6.
Каждая из следующих n строк задаёт стоимость 0≤c_i≤2⋅10^6 и объём 0<w_i≤2⋅10^6 предмета
(n, W, c_i, w_i — целые числа). Выведите максимальную стоимость частей редметов (от каждого
предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
"""
TESTING = False

COST = 0
WEIGHT = 1


def get_max_cost(capacity, things):
    things.sort(key=lambda t: -t[COST]/t[WEIGHT])

    total_cost = 0
    ratio = 1
    for thing in things:
        if capacity < thing[WEIGHT]:
            ratio = capacity / thing[WEIGHT]

        total_cost += thing[COST] * ratio
        capacity -= thing[WEIGHT] * ratio

        if ratio < 1:
            break

    return total_cost


def main():
    things_count, capacity = map(int, input().split())
    things = [tuple(map(int, input().split())) for _ in range(things_count)]
    print(round(get_max_cost(capacity, things), 3))


def test():
    import timeit

    def test_cost(expected_cost, capacity, *things):
        return round(get_max_cost(capacity, list(things)), 3) == expected_cost

    assert test_cost(180.000, 50, (60, 20), (100, 50), (120, 30))
    assert test_cost(20.005, 15.01, (10, 10), (10, 5), (10, 20))
    assert test_cost(15.545, 10, (5, 1), (10, 7), (12, 44))
    assert test_cost(30.000, 15, (10, 5), (10, 5), (10, 5))
    assert test_cost(30.000, 100500, (10, 5), (10, 5), (10, 5))
    assert test_cost(0.124, 3, (0.1002, 1), (0.0204, 1), (0.0038, 1))

    big_things_list = [(1, 1000) for _ in range(1000)]
    big_capacity = 10 ** 6
    assert test_cost(1000, big_capacity, *big_things_list)
    assert timeit.timeit(lambda: get_max_cost(big_capacity, big_things_list), number=1) < 1
    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
