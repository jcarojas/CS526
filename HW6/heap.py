import sys


class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent


class MinHeap:
    def __init__(self):
        self.root = None
        self.size = 0

    def _before(self, a, b):
        return a < b

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.size == 0:
            raise IndexError("peek from empty heap")
        return self.root.val

    def _node_at(self, pos):
        node = self.root
        for bit in bin(pos)[3:]:
            node = node.left if bit == '0' else node.right
        return node

    def _attach(self, value):
        pos = self.size + 1
        if pos == 1:
            node = Node(value)
            self.root = node
        else:
            parent = self._node_at(pos // 2)
            node = Node(value, parent)
            if pos % 2 == 0:
                parent.left = node
            else:
                parent.right = node
        self.size = pos
        return node

    def _remove_last(self):
        last = self._node_at(self.size)
        p = last.parent
        if p is None:
            self.root = None
        elif p.left is last:
            p.left = None
        else:
            p.right = None
        last.parent = None
        self.size -= 1
        return last.val

    def _sift_up(self, node):
        while node.parent and self._before(node.val, node.parent.val):
            node.val, node.parent.val = node.parent.val, node.val
            node = node.parent

    def _sift_down(self, node):
        while True:
            best = node
            if node.left and self._before(node.left.val, best.val):
                best = node.left
            if node.right and self._before(node.right.val, best.val):
                best = node.right
            if best is node:
                break
            node.val, best.val = best.val, node.val
            node = best

    def insert(self, value):
        self._sift_up(self._attach(value))

    def extract_min(self):
        if self.size == 0:
            raise IndexError("extract_min from empty heap")
        smallest = self.root.val
        v = self._remove_last()
        if self.root is not None:
            self.root.val = v
            self._sift_down(self.root)
        return smallest

    def _find(self, node, value):
        if node is None or self._before(value, node.val):
            return None
        if node.val == value:
            return node
        return self._find(node.left, value) or self._find(node.right, value)

    def delete(self, value):
        target = self._find(self.root, value)
        if target is None:
            return False
        last = self._node_at(self.size)
        v = self._remove_last()
        if last is not target:
            target.val = v
            self._sift_up(target)
            self._sift_down(target)
        return True

    def build(self, values):
        self.root, self.size = None, 0
        for v in values:
            self._attach(v)
        self._heapify(self.root)

    def _heapify(self, node):
        if node is None:
            return
        self._heapify(node.left)
        self._heapify(node.right)
        self._sift_down(node)

    def heap_sort(self):
        copy = MinHeap()
        copy.build([self._node_at(p).val for p in range(1, self.size + 1)])
        return [copy.extract_min() for _ in range(self.size)]

    def _max_width(self, node):
        if node is None:
            return 0
        return max(len(str(node.val)), self._max_width(node.left),
                   self._max_width(node.right))

    def print_heap(self):
        if self.root is None:
            print("(empty heap)")
            return
        H = self.size.bit_length()
        s = self._max_width(self.root)
        width = (2 ** H) * 2 * s + 4
        grid = [[' '] * width for _ in range(2 * H - 1)]

        def draw(node, d, c):
            txt = str(node.val)
            start = c - len(txt) // 2
            for i, ch in enumerate(txt):
                grid[2 * d][start + i] = ch
            off = (2 ** (H - 1 - d)) * s
            if node.left:
                grid[2 * d + 1][c - off // 2] = '/'
                draw(node.left, d + 1, c - off)
            if node.right:
                grid[2 * d + 1][c + off // 2] = '\\'
                draw(node.right, d + 1, c + off)

        draw(self.root, 0, (2 ** H - 2) * s + s + 1)
        for row in grid:
            print(''.join(row).rstrip())


def parse_list(text):
    text = text.strip()
    if text == "":
        return []
    inner = text[1:-1].strip()
    if inner == "":
        return []
    return [int(piece) for piece in inner.split(",")]


def main():
    values = parse_list(sys.stdin.read())
    print("Input values:", values)
    print()
    heap = MinHeap()
    for v in values:
        heap.insert(v)
        print(f"After insert({v}):")
        heap.print_heap()
        print()


if __name__ == "__main__":
    main()
