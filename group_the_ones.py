"""
binarysearch.com :: Group the Ones
jramaswami
"""


import collections


class Solution:

    def solve(self, bits, k):
        if k == 1:
            return 0

        dist = []
        first = bits.find('1')
        curr_dist = 0
        for b in bits[first+1:]:
            if b == '1':
                dist.append(curr_dist)
                curr_dist = 0
            else:
                curr_dist += 1
        w = k - 1
        print(bits)
        print(dist)
        window = collections.deque(dist[:w])
        curr_sum = soln = sum(window)
        print(window, curr_sum)
        for d in dist[w:]:
            curr_sum -= window[0]
            window.popleft()
            curr_sum += d
            window.append(d)
            soln = min(soln, curr_sum)
            print(window, curr_sum)
        return soln


def test_1():
    s = "10011"
    k = 3
    expected = 2
    assert Solution().solve(s, k) == expected


def test_2():
    s = "100111010101010101010101101111111010101011101010101"
    k = 10
    expected = 3
    assert Solution().solve(s, k) == expected