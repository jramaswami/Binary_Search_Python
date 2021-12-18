"""
binarysearch.com :: Increasing Digits
jramaswami
"""


import collections


class Solution:
    def solve(self, n):
        queue = collections.deque()
        soln = 0
        if n >= 1:
            queue.extend([(d, d, 1) for d in range(1,10)])
        while queue:
            number, last_digit, digit_count = queue.popleft()
            if digit_count == n:
                soln += 1
            if digit_count + 1 <= n:
                number0 = number * 10
                for d in range(last_digit+1, 10):
                    queue.append((number0 + d, d, digit_count + 1))
        return soln



def test_1():
    n = 2
    assert Solution().solve(n) == 36


def test_2():
    n = 0
    assert Solution().solve(n) == 0


def test_3():
    n = 1
    assert Solution().solve(n) == 9
