import collections


class Heap(object):
    # Direction of balancing
    UP = 1
    DOWN = 2

    def __init__(self):
        self._data = collections.deque()
        self._len = 0

    def __len__(self):
        return self._len

    def _get_parent(self, index):
        if 0 < index < len(self):
            return (index - 1) // 2

    def _get_appropriate_child(self, index):
        left = index * 2 + 1
        right = (index + 1) * 2
        if left >= len(self):
            return None
        elif right >= len(self) or self._data[left] > self._data[right]:
            return left
        else:
            return right

    def _balance_edge(self, child_index, parent_index):
        if (
            child_index is not None and
            parent_index is not None and
            self._data[parent_index] < self._data[child_index]
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

    def insert(self, precedence):
        self._data.append(precedence)
        self._len += 1
        self._balance_item(len(self) - 1, self.UP)

    def insert_items(self, items):
        for item in items:
            if isinstance(item, collections.Iterable):
                self.insert(*item)
            else:
                self.insert(item)

    def update(self, index, precedence):
        if self._data[index] != precedence:
            self._data[index] = precedence
            self._balance_item(index)

    def get_top(self):
        if self._data:
            return self._data[0]

    def extract_top(self):
        if self._data:
            data = self._data.popleft()
            self._len -= 1
            self._data.rotate(1)
            self._balance_item(0, self.DOWN)
            return data

    def remove(self, index):
        self.update(index, float('infinity'))
        self.extract_top()
