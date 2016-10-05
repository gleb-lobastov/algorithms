import collections


class Heap(object):
    # Order of heap. This numbers is used in unit testing
    MIN = 0
    MAX = 1

    # Direction of balancing
    UP = 1
    DOWN = 2

    def __init__(self, order=MAX, arity=2):
        assert arity >= 2
        assert order in (self.MIN, self.MAX)
        self._data = collections.deque()
        self._arity = arity
        self._order = order

    def __len__(self):
        return len(self._data)

    def _get_precedence(self, index):
        precedence, _ = self._data[index]
        return precedence

    def _set_precedence(self, index, new_precedence):
        old_precedence, payload = self._data[index]
        if old_precedence == new_precedence:
            return False

        self._data[index] = new_precedence, payload
        return True

    def _get_parent(self, index):
        if 0 < index < len(self):
            return (index - 1) // self._arity

    def _get_childes(self, index):
        max_index = len(self)
        return range(
            min(max_index, index * self._arity + 1),
            min(max_index, (index + 1) * self._arity + 1)
        )

    def _get_appropriate_child(self, index):
        comparison = max if self._order == self.MAX else min
        return comparison(
            ((self._get_precedence(child_index), child_index) for child_index in self._get_childes(index)),
            default=(None, None)  # Case, when deal with leaf (no childes)
        )[1]

    def _is_balanced(self, child_index, parent_index):
        child, parent = self._get_precedence(child_index), self._get_precedence(parent_index)
        if self._order == self.MAX:
            return parent >= child
        else:
            return child >= parent

    def _balance_edge(self, child_index, parent_index):
        if (
            child_index is not None and
            parent_index is not None and
            not self._is_balanced(child_index, parent_index)
        ):
            self._data[child_index], self._data[parent_index] = self._data[parent_index], self._data[child_index]
            return child_index, parent_index
        else:
            return None, None

    def _balance_item(self, index, direction=None):
        index_up = index_down = index

        # Floating
        if direction != self.DOWN:
            while index_up:  # Stops at 0 as index and None as mark of balanced edge
                _, index_up = self._balance_edge(index_up, self._get_parent(index_up))

        # Sinking
        if direction != self.UP:
            while index_down is not None:  # Shouldn't stop at 0
                index_down, _ = self._balance_edge(self._get_appropriate_child(index_down), index_down)

    def insert(self, precedence, payload=None):
        self._data.append((precedence, payload))
        self._balance_item(len(self) - 1, self.UP)

    def insert_items(self, items):
        for item in items:
            if isinstance(item, collections.Iterable):
                self.insert(*item)
            else:
                self.insert(item)

    def update(self, index, precedence):
        if self._set_precedence(index, precedence):
            self._balance_item(index)

    def get_top(self):
        if self._data:
            _, payload = self._data[0]
            return payload

    def extract_top(self):
        if self._data:
            _, payload = self._data.popleft()
            self._data.rotate(1)
            self._balance_item(0, self.DOWN)
            return payload

    def remove(self, index):
        self.update(index, float('infinity') if self._order == self.MAX else float('-infinity'))
        self.extract_top()
