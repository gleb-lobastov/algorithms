"""
По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита,
постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k,
встречающихся в строке, и размер получившейся закодированной строки. В следующих k строках запишите
коды букв в формате "letter: code". В последней строке выведите закодированную строку.
"""
import sys
import bisect
from collections import deque as deque_original

TESTING = False


class Deque35(deque_original):
    """ Эмуляция deque.insert из питона 3.5 """
    def insert(self, index, value):
        n = len(self)
        if index >= n:
            return self.append(value)

        if index <= -n or index == 0:
            return self.appendleft(value)

        self.rotate(-index)

        if index < 0:
            self.append(value)
        else:
            self.appendleft(value)

        self.rotate(index)
        return None

deque = Deque35 if sys.version_info < (3, 5) else deque_original


class TreeItem(object):
    def __init__(self, key):
        self._key = key

    def __int__(self):
        return self._key

    def __gt__(self, other):
        return self._key > int(other)

    def __eq__(self, other):
        return self._key == int(other)


class BinaryNode(TreeItem):
    def __init__(self, *subs):
        assert len(subs) == 2
        super().__init__(sum(map(int, subs)))
        self._subs = subs

    def __repr__(self):
        return '{}: [{}]'.format(self._key, ', '.join(repr(sub) for sub in self._subs))

    def flatten(self):
        return [
            '{}{}'.format(index, value)
            for index, sub in enumerate(self._subs)
            for value in sub.flatten()
        ]


class Leaf(TreeItem):
    def __init__(self, key, value):
        super().__init__(key)
        self._value = value

    def __repr__(self):
        return str('{}: {}'.format(self._key, self._value))

    def flatten(self):
        return self._value,


def create_encoding(decoded):
    frequency_tree = deque(sorted(
        (Leaf(decoded.count(letter), letter) for letter in set(decoded)),
        key=int
    ))
    while len(frequency_tree) > 1:
        node = BinaryNode(frequency_tree.popleft(), frequency_tree.popleft())
        bisect.insort(frequency_tree, node)

    root = frequency_tree[0]
    return {code[-1]: code[:-1] or '0' for code in root.flatten()}


def encode(string, encoding):
    return ''.join(encoding[letter] for letter in string)


def main():
    decoded = input()
    encoding = create_encoding(decoded)
    encoded = encode(decoded, encoding)
    print(len(encoding), len(encoded), sep=' ')
    for letter, code in encoding.items():
        print(letter, code, sep=': ')
    print(encoded)


def test():
    import timeit
    import string
    import random

    def random_str(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def test_encoder(decoded, *encoded):
        return encode(decoded, create_encoding(decoded)) in encoded

    assert test_encoder('a', '0')
    assert test_encoder('abb', '011')
    assert test_encoder('aab', '110')
    assert test_encoder('abcc', '101100', '111000')
    assert test_encoder('abacabad', '01001100100111', '01001110100110')

    assert timeit.timeit(lambda: test_encoder(random_str(10000), 'whatever'), number=1) < 1
    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
