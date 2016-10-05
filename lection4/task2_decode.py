"""
Восстановите строку по её коду и беспрефиксному коду символов.

В первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв,
встречающихся в строке, и размер получившейся закодированной строки, соответственно. В следующих k
строках записаны коды букв в формате "letter: code". Ни один код не является префиксом другого. Буквы
могут быть перечислены в любом порядке. В качестве букв могут встречаться лишь строчные буквы латинского
алфавита; каждая из этих букв встречается в строке хотя бы один раз. Наконец, в последней строке записана
закодированная строка. Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная
строка имеет минимальный возможный размер.


В первой строке выходного файла выведите строку ss. Она должна состоять из строчных букв латинского алфавита.
Гарантируется, что длина правильного ответа не превосходит 10^4 символов.
"""
import sys
import bisect
from collections import deque as deque_original

TESTING = False

LEFT = '0'
RIGHT = '1'


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

    def find_bit(self, bit):
        assert bit in [LEFT, RIGHT]
        return self._subs[int(bit)]


class Leaf(TreeItem):
    def __init__(self, key, value):
        super().__init__(key)
        self._value = value

    def __repr__(self):
        return str('{}: {}'.format(self._key, self._value))

    def flatten(self):
        return self._value,

    @property
    def value(self):
        return self._value


def get_side(code):
    for side in (LEFT, RIGHT):
        if code.startswith(side):
            return side
    return None


def _build_tree_item(codes, path):
    if len(codes) == 1 and get_side(codes[0]) is None:
        return Leaf(0, codes[0])

    left, right = [], []
    for code in codes:
        side, rest = get_side(code), code[1:]
        if side is None:
            raise ValueError('Structure error: code: {}, codes: {}, path: {}'.format(code, codes, path))

        (left if side is LEFT else right).append(rest)

    return BinaryNode(
        _build_tree_item(left, path + LEFT),
        _build_tree_item(right, path + RIGHT)
    )


def build_tree(codes):
    if len(codes) == 1:
        return Leaf(0, codes[0].lstrip('01'))
    return _build_tree_item(codes, '')


def decode(encoded, codes):
    decoded = ''
    item = tree = build_tree(codes)

    for bit in encoded:
        if isinstance(item, BinaryNode):
            item = item.find_bit(bit)
        if isinstance(item, Leaf):
            decoded += item.value
            item = tree

    return decoded


def main():
    letter_count, _ = map(int, input().split())
    codes = ['{1}{0}'.format(*input().split(': ')) for _ in range(letter_count)]
    encoded = input()
    print(decode(encoded, codes))


def test():
    import timeit
    import string
    import random
    import _1_encode

    def random_str(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def test_decoder(decoded, encoded, codes):
        return decode(encoded, codes) == decoded

    assert test_decoder('a', '0', ['0a'])
    assert test_decoder('abacabad', '01001100100111', ['0a', '10b', '110c', '111d'])

    test_decoded = random_str(10000)
    test_encoding = _1_encode.create_encoding(test_decoded)
    test_encoded = _1_encode.encode(test_decoded, test_encoding)
    test_codes = [code + letter for letter, code in test_encoding.items()]
    assert timeit.timeit(lambda: test_decoder(test_decoded, test_encoded, test_codes), number=1) < 1
    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
