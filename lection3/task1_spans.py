"""
По данным n отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит
по два числа 0≤l≤r≤10^9, задающих начало и конец отрезка. Выведите оптимальное
число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.
"""
TESTING = False

START = 0
END = 1


def get_points(spans):
    points = []
    if not spans:
        return points

    spans.sort()

    max_expected_point = spans[0][END]
    for span in spans:
        if span[START] > max_expected_point:
            points.append(max_expected_point)
            max_expected_point = span[END]
        else:
            max_expected_point = min(max_expected_point, span[END])

    points.append(max_expected_point)
    return points


def main():
    spans_count = int(input())
    spans = [tuple(sorted(map(int, input().split()))) for _ in range(spans_count)]
    points = get_points(spans)
    print(len(points))
    print(*points, sep=' ')


def test():
    def test_points(expected_len, *spans):
        return len(get_points(list(spans))) == expected_len

    assert test_points(0)
    assert test_points(1, (1, 1))
    assert test_points(1, (1, 2))
    assert test_points(2, (1, 2), (3, 4))
    assert test_points(1, (1, 3), (2, 4))
    assert test_points(1, (1, 2), (2, 4))
    assert test_points(1, (1, 10), (1, 5), (1, 2))
    assert test_points(1, (1, 10), (2, 10), (5, 10))
    assert test_points(3, (50, 55), (20, 25), (5, 10))
    assert test_points(2, (1, 6), (2, 5), (4, 8), (7, 10))
    assert test_points(2, (1, 6), (2, 5), (5, 8), (7, 10))
    assert test_points(2, (1, 6), (2, 5), (6, 8), (7, 10))
    assert test_points(1, (1, 3), (2, 5), (3, 6))
    assert test_points(2, (4, 7), (1, 3), (2, 5), (5, 6))

    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
