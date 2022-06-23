"""
binarysearch.com :: Least Frequently Used Cache
jramaswami
"""


import collections


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_value = dict()
        self.key_freqs = dict()
        self.freqs_list = collections.defaultdict(collections.deque)
        self.min_freq = 0

    def get(self, key):
        if key in self.key_value:
            self._increment_use(key)
            return self.key_value[key]
        else:
            return -1

    def set(self, key, val):
        if key not in self.key_value and len(self.key_value) == self.capacity:
            self._eject()
        self._increment_use(key)
        self.key_value[key] = val

    def _increment_use(self, key):
        if key not in self.key_value:
            self.key_freqs[key] = 1
            self.freqs_list[1].append(key)
            self.min_freq = 1
        else:
            prev_freq = self.key_freqs[key]
            i = self.freqs_list[prev_freq].index(key)
            self.freqs_list[prev_freq][i] = None
            while self.freqs_list[prev_freq] and self.freqs_list[prev_freq][0] is None:
                self.freqs_list[prev_freq].popleft()
            if not self.freqs_list[self.min_freq]:
                del self.freqs_list[self.min_freq]
                self.min_freq += 1
            self.freqs_list[prev_freq + 1].append(key)
            self.key_freqs[key] = prev_freq + 1

    def _eject(self):
        ejecting_key = self.freqs_list[self.min_freq].popleft()
        while self.freqs_list[self.min_freq] and self.freqs_list[self.min_freq][0] is None:
            self.freqs_list[self.min_freq].popleft()
        if not self.freqs_list[self.min_freq]:
            del self.freqs_list[self.min_freq]
            self.min_freq += 1
        del self.key_value[ejecting_key]
        del self.key_freqs[ejecting_key]


def test_1():
    methods = ["constructor", "set", "get", "set", "set", "set", "get", "get"]
    arguments = [[3], [1, 10], [1], [2, 20], [3, 30], [4, 40], [3], [2]]
    expected =[None, None, 10, None, None, None, 30, -1]
    cache = LFUCache(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(cache, m)(*a)
        print(f"cache.{m}({a}) {r} =? {e}")
        assert r == e


def test_2():
    "WA"
    methods = ["constructor","get","set","get","set","get"]
    arguments = [[1],[1],[2,5],[2],[0,0],[2]]
    expected = [None, -1, None, 5, None, -1]
    cache = LFUCache(*arguments[0])
    print(f"LFUCache({arguments[0]})")
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(cache, m)(*a)
        print(f"cache.{m}({a}) {r} =? {e}")
        assert r == e
