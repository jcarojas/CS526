import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        self.root, added = self._add(self.root, value)
        return added

    def _add(self, node, value):
        if node is None:
            return Node(value), True
        added = False
        if value < node.value:
            node.left, added = self._add(node.left, value)
        elif value > node.value:
            node.right, added = self._add(node.right, value)
        return node, added

    def find_node(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def delete_node(self, value):
        self.root, deleted = self._delete(self.root, value)
        return deleted

    def _delete(self, node, value):
        if node is None:
            return None, False
        if value < node.value:
            node.left, deleted = self._delete(node.left, value)
            return node, deleted
        if value > node.value:
            node.right, deleted = self._delete(node.right, value)
            return node, deleted

        if node.left is None:
            return node.right, True
        if node.right is None: 
            return node.left, True

        successor = node.right
        while successor.left is not None:
            successor = successor.left
        node.value = successor.value
        node.right, _ = self._delete(node.right, successor.value)
        return node, True

    def print_tree(self):
        if self.root is None:
            print("    (empty tree)")
        else:
            self._print(self.root, 0)

    def _print(self, node, depth):
        if node is None:
            return
        self._print(node.right, depth + 1)
        print("    " + "      " * depth + str(node.value))
        self._print(node.left, depth + 1)

def main():
    size = random.randint(5, 50)
    values = random.sample(range(1, 1001), size)

    print("Input set (" + str(size) + " numbers):")
    print(values)

    tree = BST()
    for v in values:
        tree.add_node(v)
    present = list(values)

    print("\nInitial tree (sideways, root at the left):")
    tree.print_tree()

    print("\nAdd in Values:")
    for _ in range(3):
        new_value = random.randint(1, 1000)
        print("\nadd_node(" + str(new_value) + ")")
        if tree.add_node(new_value):
            present.append(new_value)
        else:
            print("  " + str(new_value) + " is already in the tree, nothing added")
        tree.print_tree()

    print("\nDelete values:")
    root_value = tree.root.value
    targets = [root_value] + random.sample([p for p in present if p != root_value], 3)
    for t in targets:
        print("\ndelete_node(" + str(t) + ")")
        tree.delete_node(t)
        present.remove(t)
        tree.print_tree()

    missing = random.randint(1, 1000)
    while missing in present:
        missing = random.randint(1, 1000)
    print("\ndelete_node(" + str(missing) + ")  (not in the tree)")
    if not tree.delete_node(missing):
        print("  " + str(missing) + " was not found, tree unchanged")
    tree.print_tree()

    print("\nFind values:")
    guesses = [random.randint(1, 1000) for _ in range(3)]
    guesses.append(random.choice(present))
    for g in guesses:
        if tree.find_node(g):
            print("find_node(" + str(g) + "): FOUND")
        else:
            print("find_node(" + str(g) + "): NOT FOUND")

main()
