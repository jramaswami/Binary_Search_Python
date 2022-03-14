"""
binarysearch.com :: Ways to Sum Consecutive Numbers to N
jramaswami
"""


import collections


class Solution():
    def solve(self, N):
        window = collections.deque()
        curr_sum = 0
        soln = 0
        for n in range(1, N+1):
            window.append(n)
            curr_sum += n
            while curr_sum > N:
                curr_sum -= window[0]
                window.popleft()

            if curr_sum == N:
                # print(window)
                soln += 1

        return soln


def test_1():
    n = 9
    expected = 3
    assert Solution().solve(n) == expected


def test_2():
    n = 2147483648
    expected = 2
    assert Solution().solve(n) == expected
