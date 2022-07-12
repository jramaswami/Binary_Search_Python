"""
binarysearch.com :: Angry Owner
jramaswami
"""


import collections
import itertools



class Solution:

    def solve(self, customers, mood, k):
        if not customers or not mood:
            return 0

        if not k:
            return sum(c * h for c, h in zip(customers, mood))

        happy_customers = [c * h for c, h in zip(customers, mood)]
        prefix = list(itertools.accumulate(happy_customers))
        suffix = list(itertools.accumulate(reversed(happy_customers)))[::-1]

        def get_prefix(i):
            if i < 0:
                return 0
            return prefix[i]

        def get_suffix(i):
            if i >= len(suffix):
                return 0
            return suffix[i]

        window = collections.deque(enumerate(customers[:k]))
        window_sum = sum(customers[:k])
        soln = window_sum + get_suffix(window[0][0]+1)
        for right, n in enumerate(customers[k:], start=k):
            window_sum -= window[0][1]
            window.popleft()
            window.append((right, n))
            window_sum += n
            left = window[0][0]
            x = get_prefix(left - 1) + window_sum + get_suffix(right+1)
            soln = max(x, soln)
        return soln


def test_1():
    customers = [1, 2, 5, 5, 2]
    mood = [1, 1, 0, 0, 0]
    k = 2
    expected = 13
    assert Solution().solve(customers, mood, k) == expected


def test_2():
    "WA"
    customers = []
    mood = []
    k = 0
    expected = 0
    assert Solution().solve(customers, mood, k) == expected


def test_3():
    customers = [1, 2, 5, 5, 2]
    mood = [1, 1, 0, 0, 0]
    k = 0
    expected = 3
    assert Solution().solve(customers, mood, k) == expected


def test_4():
    "WA"
    customers = [1, 2]
    mood = [0, 1]
    k = 2
    expected = 3
    assert Solution().solve(customers, mood, k) == expected
