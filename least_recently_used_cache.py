"""
binarysearch.com :: Least Recently Used Cache
jramaswami
"""
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_after(self, node, new_node):
        new_node.prev = node
        if node.next is None:
            new_node.next = None
            self.tail = new_node
        else:
            new_node.next = node.next
            node.next.prev = new_node
        node.next = new_node
        self.size += 1

    def insert_before(self, node, new_node):
        new_node.next = node
        if node.prev is None:
            new_node.prev = None
            self.head = new_node
        else:
            new_node.prev = node.prev
            node.prev.next = new_node
        node.prev = new_node
        self.size += 1

    def insert_beginning(self, new_node):
        if self.head is None:
            self.head = self.tail = new_node
            self.size += 1
        else:
            self.insert_before(self.head, new_node)

    def insert_end(self, new_node):
        if self.tail is None:
            self.insert_beginning(new_node)
        else:
            self.insert_after(self.tail, new_node)

    def remove(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1

    def pop_front(self):
        if self.head is None:
            raise ValueError
        node = self.head
        self.remove(node)
        node.next = None
        return node

    def pop_back(self):
        if self.tail is None:
            raise ValueError
        node = self.tail
        self.remove(node)
        node.next = None
        return node

    def __len__(self):
        return self.size

    def __repr__(self):
        arr = []
        curr_node = self.head
        while curr_node:
            arr.append(curr_node)
            curr_node = curr_node.next
        return f"DoublyLinkedList({arr}, size={self.size}, head={self.head} tail={self.tail})"


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node(key={self.key}, val={self.val})"


class LRUCache:
    def __init__(self, capacity):
        self.cache = DoublyLinkedList()
        self.keys = dict()
        self.capacity = capacity

    def get(self, key):
        if key in self.keys:
            return self.keys[key].val
        else:
            return -1

    def set(self, key, val):
        if key in self.keys:
            node = self.keys[key]
            node.val = val
            self.cache.remove(node)
        else:
            node = Node(key, val)
            self.keys[key] = node
        self.cache.insert_beginning(node)
        while len(self.cache) > self.capacity:
            old_node = self.cache.pop_back()
            self.keys.pop(old_node.key)

    def __repr__(self):
        return f"LRUCache(capacity={self.capacity}, keys={self.keys}, cache={self.cache})"


#
# Testing
# 

def test_1():
    methods = ["constructor", "set", "get", "set", "set", "set", "get", "get"]
    arguments = [[3], [1, 10], [1], [2, 20], [3, 30], [4, 40], [1], [4]]
    expected = [None, None, 10, None, None, None, -1, 40]

    lru = LRUCache(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        print(f"lru.{m}({a}) == {e}")
        assert getattr(lru, m)(*a) == e


def test_2():
    methods = ["constructor", "set", "set", "get"]
    arguments = [[2], [4, 0], [4, 4], [3]]
    expected = [None, None, None, -1]

    lru = LRUCache(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        print(f"lru.{m}({a}) == {e}")
        assert getattr(lru, m)(*a) == e


def test_3():
    methods = ["constructor", "get", "set", "set", "set", "set"]
    arguments = [[4], [4], [3, 0], [2, 8], [0, 9], [2, 7]]
    expected = [None, -1, None, None, None, None]

    lru = LRUCache(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        print(f"lru.{m}({a}) == {e}")
        assert getattr(lru, m)(*a) == e
