import unittest
import collections
from heap import Heap

GET_PAYLOAD = 1

PARENT_IDX = 0
SELF_IDX = 1
SIBLING_IDX = 2
LIGHT_CHILD_IDX = 3
HEAVY_CHILD_IDX = 4
LAST_ITEM_IDX = 5

TOP = 10, 100
XS = 25, 75
S = 35, 65
M = 50, 50
L = 65, 35
XL = 75, 25

valid_data = {order: collections.deque([
    (TOP[order], PARENT_IDX),
    (M[order], SELF_IDX),
    (XS[order], SIBLING_IDX),
    (L[order], LIGHT_CHILD_IDX),
    (XL[order], HEAVY_CHILD_IDX),
    (S[order], LAST_ITEM_IDX)
]) for order in (Heap.MIN, Heap.MAX)}


class TestRelatives(unittest.TestCase):
    def setUp(self):
        self.heap = Heap(order=Heap.MAX, arity=2)
        self.heap._data = valid_data[Heap.MAX].copy()

    def test_1(self):
        """ Checking parent node lookup """
        self.assertEqual(self.heap._get_parent(SELF_IDX), PARENT_IDX)

    def test_2a(self):
        """ Checking child nodes lookup (a)"""
        self.assertSetEqual(set(self.heap._get_childes(SELF_IDX)), {HEAVY_CHILD_IDX, LIGHT_CHILD_IDX})

    def test_2b(self):
        """ Checking child nodes lookup (b)"""
        self.assertSetEqual(set(self.heap._get_childes(PARENT_IDX)), {SELF_IDX, SIBLING_IDX})

    def test_2c(self):
        """ Checking child nodes lookup (c), for partial filling """
        self.assertSetEqual(set(self.heap._get_childes(SIBLING_IDX)), {LAST_ITEM_IDX})

    def test_2d(self):
        """ Checking child nodes lookup (c), for leaf """
        self.assertFalse(bool(self.heap._get_childes(LAST_ITEM_IDX)))

    def test_3(self):
        """ Checking lookup for child node, that appropriate for balancing """
        self.assertEqual(self.heap._get_appropriate_child(SELF_IDX), LIGHT_CHILD_IDX)


class TestingHeap(Heap):
    def __init__(self, data, **specification):
        super().__init__(**specification)
        self._data = data

    def _count_unbalanced_edges(self, index=0):
        childes = tuple(self._get_childes(index))
        unbalanced = int(any(not self._is_balanced(child_index, index) for child_index in childes))
        return unbalanced + sum(self._count_unbalanced_edges(child_index) for child_index in childes)

    def _balance_edge(self, child_index, parent_index):
        result = super()._balance_edge(child_index, parent_index)
        assert self._count_unbalanced_edges() <= 1
        return result

    def assert_balanced(self):
        assert self._count_unbalanced_edges() == 0

    @property
    def precedence(self):
        """ Unit that increase precedence of item """
        return 1 if self._order == Heap.MAX else -1


class TestBalancing(unittest.TestCase):
    def setUp(self):
        self.heaps = {
            order: TestingHeap(valid_data[order].copy(), order=order, arity=2)
            for order in(Heap.MIN, Heap.MAX)
        }

    def test1(self):
        """ check comparison """
        for heap in self.heaps.values():
            self.assertTrue(heap._is_balanced(SELF_IDX, PARENT_IDX))

    def test_1a(self):
        """ pop up once """
        for order, heap in self.heaps.items():
            heap.update(SELF_IDX, TOP[order] + heap.precedence)
            heap.assert_balanced()
            self.assertEqual(heap._data[PARENT_IDX][GET_PAYLOAD], SELF_IDX)
            self.assertEqual(heap._data[SELF_IDX][GET_PAYLOAD], PARENT_IDX)

    def test_1b(self):
        """ pop up loop """
        for order, heap in self.heaps.items():
            heap.update(HEAVY_CHILD_IDX, TOP[order] + heap.precedence)
            heap.assert_balanced()
            self.assertEqual(heap._data[PARENT_IDX][GET_PAYLOAD], HEAVY_CHILD_IDX)

    def test_2a(self):
        """ dip down once """
        for order, heap in self.heaps.items():
            heap.update(SELF_IDX, XL[order] - heap.precedence)
            heap.assert_balanced()
            self.assertEqual(heap._data[LIGHT_CHILD_IDX][GET_PAYLOAD], SELF_IDX)
            self.assertEqual(heap._data[SELF_IDX][GET_PAYLOAD], LIGHT_CHILD_IDX)

    def test_2b(self):
        """ dip down loop """
        for order, heap in self.heaps.items():
            heap.update(PARENT_IDX, XL[order] - heap.precedence)
            heap.assert_balanced()
            self.assertEqual(heap._data[LAST_ITEM_IDX][GET_PAYLOAD], PARENT_IDX)
            self.assertEqual(heap._data[PARENT_IDX][GET_PAYLOAD], SIBLING_IDX)

    def test_3(self):
        """ stay on """
        for heap in self.heaps.values():
            heap._balance_item(SELF_IDX)
            heap.assert_balanced()
            self.assertEqual(heap._data[SELF_IDX][GET_PAYLOAD], SELF_IDX)
