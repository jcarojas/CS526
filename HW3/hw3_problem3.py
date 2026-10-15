#!/usr/bin/env python
# coding: utf-8

# In[2]:


class ArrayStack:
    
    def __init__(self, capacity=10):
        self._data = [None] * max(1, capacity)
        self._size = 0

    def push(self, value):
        if self._size == len(self._data):
            bigger = [None] * (len(self._data) * 2)
            self._copy(self._data, bigger, 0)
            self._data = bigger
        self._data[self._size] = value
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        self._size -= 1
        value = self._data[self._size]
        self._data[self._size] = None
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[self._size - 1]

    def is_empty(self):
        return self._size == 0

    def _copy(self, src, dst, i):
        if i >= self._size:
            return
        dst[i] = src[i]
        self._copy(src, dst, i + 1)

    def reverse(self):
        self._reverse_range(0, self._size - 1)

    def _reverse_range(self, left, right):
        if left >= right:
            return
        self._data[left], self._data[right] = self._data[right], self._data[left]
        self._reverse_range(left + 1, right - 1)

    def to_list(self):
        result = [None] * self._size
        self._copy(self._data, result, 0)
        return result


class _SNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedStack:
    def __init__(self):
        self._head = None

    def push(self, value):
        node = _SNode(value)
        node.next = self._head
        self._head = node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def reverse(self):
        self._head = self._reverse(self._head, None)

    def _reverse(self, node, prev):
        if node is None:  
            return prev
        nxt = node.next
        node.next = prev
        return self._reverse(nxt, node)

    def to_list(self):
        return self._collect(self._head)

    def _collect(self, node):
        if node is None:
            return []
        return self._collect(node.next) + [node.value]


class _DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedStack:
    def __init__(self):
        self._head = None
        self._tail = None

    def push(self, value):
        node = _DNode(value)
        node.next = self._head
        if self._head is not None:
            self._head.prev = node
        else:
            self._tail = node
        self._head = node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        else:
            self._tail = None
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def reverse(self):
        self._swap_links(self._head)
        self._head, self._tail = self._tail, self._head

    def _swap_links(self, node):
        if node is None:
            return
        node.prev, node.next = node.next, node.prev
        self._swap_links(node.prev)

    def to_list(self):
        return self._collect(self._tail)

    def _collect(self, node):
        if node is None:
            return []
        return [node.value] + self._collect(node.prev)

def push_all(stack, values, i=0):
    if i >= len(values):
        return
    stack.push(values[i])
    push_all(stack, values, i + 1)

def show(label, stack):
    print(label + ":", ", ".join(map(str, stack.to_list())))

def run(name, stack):
    print(name)
    push_all(stack, list(range(1, 11)))
    show("Before", stack)
    stack.reverse()
    show("After", stack)
    print()

def main():
    run("Array stack", ArrayStack())
    run("Singly linked list stack", SinglyLinkedStack())
    run("Doubly linked list stack", DoublyLinkedStack())

if __name__ == "__main__":
    main()

