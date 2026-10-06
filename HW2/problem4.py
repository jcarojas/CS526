#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None   # previous Node (None if first)
        self.next = None   # next Node (None if last)


class SortedDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def add(self, value):
        new = Node(value)

        current = self.head
        while current is not None and current.value <= value:
            current = current.next

        if current is None:
            new.prev = self.tail
            if self.tail is not None:
                self.tail.next = new
            else:
                self.head = new
            self.tail = new
        else:
            new.next = current
            new.prev = current.prev
            if current.prev is not None:
                current.prev.next = new
            else:
                self.head = new
            current.prev = new
        self._size += 1

    def exists(self, value):
        return self._find_node(self.head, value) is not None

    def _find_node(self, current, value):
        if current is None or current.value > value:   # sorted: can stop early
            return None
        if current.value == value:
            return current
        return self._find_node(current.next, value)

    def count(self, value):
        return self._count(self.head, value)

    def _count(self, current, value):
        if current is None or current.value > value:   # sorted: can stop early
            return 0
        return (1 if current.value == value else 0) + self._count(current.next, value)

    def total(self):
        return self._total(self.head)

    def _total(self, current):
        if current is None:
            return 0
        return current.value + self._total(current.next)

    def print_list(self):
        if self.head is None:
            print("(empty)")
        else:
            print(self._to_string(self.head))

    def _to_string(self, current):
        if current.next is None:
            return str(current.value)
        return str(current.value) + " <-> " + self._to_string(current.next)

    def _node_at(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def sum_middle_three(self):
        n = self._size
        if n < 3:
            raise ValueError("need at least 3 nodes")
        mid = n // 2
        start = mid - 1 if n % 2 == 1 else mid - 2
        node = self._node_at(start)
        return node.value + node.next.value + node.next.next.value

    def median(self):
        n = self._size
        if n == 0:
            raise ValueError("median of an empty list")
        mid = n // 2
        if n % 2 == 1:
            return self._node_at(mid).value
        node = self._node_at(mid - 1)
        return (node.value + node.next.value) / 2

    def delete(self, value):
        """Remove one node holding value. True if removed, else False."""
        node = self._find_node(self.head, value)
        if node is None:
            return False
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self._size -= 1
        return True

