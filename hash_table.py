"""
binarysearch.com :: Hash Table
jramaswami
"""


class Entry:
    def __init__(self, k, v):
        self.key = k
        self.val = v


class HashTable:
    def __init__(self):
        self.M = 1129
        self.buckets = [[] for _ in range(self.M)]

    def _find(self, key):
        bid = key % self.M
        i = 0
        while i < len(self.buckets[bid]):
            if self.buckets[bid][i].key == key:
                return bid, i
            i += 1
        return bid, i

    def put(self, key, val):
        bid, i = self._find(key)
        if i >= len(self.buckets[bid]):
            self.buckets[bid].append(Entry(key,val))
        else:
            self.buckets[bid][i].val = val

    def get(self, key):
        bid, i = self._find(key)
        if i < len(self.buckets[bid]):
            return self.buckets[bid][i].val
        return -1

    def remove(self, key):
        bid, i = self._find(key)
        if i < len(self.buckets[bid]):
            self.buckets[bid][i], self.buckets[bid][-1] = self.buckets[bid][-1], self.buckets[bid][i]
            self.buckets[bid].pop()
