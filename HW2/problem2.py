#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index is out of range")
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            prev = self._node_at(index - 1)
            node = Node(value)
            node.next = prev.next
            prev.next = node
            self.length += 1

    def get(self, index):
        self._check_index(index)
        return self._node_at(index).value

    def find(self, value):
        current = self.head
        position = 0
        while current:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1

    def __len__(self):
        return self.length

     def update(self, index, value):
        self._check_index(index)
        self._node_at(index).value = value

    def delete(self, value):
        prev = None
        current = self.head
        while current:
            if current.value == value:
                self._unlink(prev, current)
                return True
            prev = current
            current = current.next
        return False

    def delete_at(self, index):
        self._check_index(index)
        prev = self._node_at(index - 1) if index > 0 else None
        current = prev.next if prev else self.head
        self._unlink(prev, current)
        return current.value

     def print_list(self):
       if self.head is None:
            print("(empty)")
            return
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values))

    def _check_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")

    def _node_at(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def _unlink(self, prev, current):
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        if current is self.tail:
            self.tail = prev
        self.length -= 1


if __name__ == "__main__":
    lst = SinglyLinkedList()

