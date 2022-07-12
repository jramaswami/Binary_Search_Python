"""
binarysearch.com :: Ticket Order
jramaswami
"""


import collections


class Bucket:

    NUM_BUCKETS = 317

    def __init__(self):
        self.buckets = [collections.defaultdict(int) for _ in range(Bucket.NUM_BUCKETS)]
        self.bucket_sum = [0 for _ in range(Bucket.NUM_BUCKETS)]
        self.bucket_size = [0 for _ in range(Bucket.NUM_BUCKETS)]

    def add(self, x):
        bucket_id = x // Bucket.NUM_BUCKETS
        self.buckets[bucket_id][x] += 1
        self.bucket_size[bucket_id] += 1
        self.bucket_sum[bucket_id] += x

    def query(self, x):
        bucket_id = x // Bucket.NUM_BUCKETS
        sum_lt_x = 0
        size_gte_x = 0
        # Check the x's bucket first.
        for k in self.buckets[bucket_id]:
            if k < x:
                sum_lt_x += (k * self.buckets[bucket_id][k])
            else:
                size_gte_x += self.buckets[bucket_id][k]

        # Check buckets less than x.
        sum_lt_x += sum(self.bucket_sum[:bucket_id])
        size_gte_x += sum(self.bucket_size[bucket_id+1:])
        return sum_lt_x + (x * size_gte_x)

    def __repr__(self):
        return f"Bucket({list(zip(self.buckets, self.bucket_size, self.bucket_sum))})"


class Solution:
    def solve(self, tickets):
        fwd_bucket = Bucket()
        soln = list(tickets)
        for i, t in enumerate(tickets):
            soln[i] += fwd_bucket.query(t)
            fwd_bucket.add(t)
        bkw_bucket = Bucket()
        for i in range(len(tickets)-1, -1, -1):
            t = tickets[i]
            soln[i] += bkw_bucket.query(t-1)
            bkw_bucket.add(t)
        return soln


#
# Testing
#


import random


def brute_force(tickets):
        tickets0 = collections.deque(enumerate(tickets))
        soln = [0 for _ in tickets]
        time = 1
        while tickets0:
            i, x = tickets0.popleft()
            if x - 1 == 0:
                soln[i] = time
            else:
                tickets0.append((i, x - 1))
            time += 1
        return soln


def test_1():
    tickets = [2, 1, 2]
    expected = [4, 2, 5]
    assert Solution().solve(tickets) == expected


def test_2():
    for _ in range(100):
        tickets = [random.randint(1, 100) for _ in range(1000)]
        expected = brute_force(tickets)
    assert Solution().solve(tickets) == expected


def test_3():
    for _ in range(10):
        tickets = [random.randint(1, 100) for _ in range(10000)]
        expected = brute_force(tickets)
    assert Solution().solve(tickets) == expected


def test_4():
    for _ in range(100):
        N = random.randint(0, 100)
        tickets = [random.randint(1, 1000) for _ in range(N)]
        expected = brute_force(tickets)
    assert Solution().solve(tickets) == expected


def test_5():
    tickets = []
    expected = brute_force(tickets)
    assert Solution().solve(tickets) == expected
