"""
binarysearch.com :: Kth Permutation Sequence
jramaswami
"""


import math


class Solution:

    def solve(self, n, k):
        soln = []
        numbers = list(range(1,n+1))
        cycle = math.prod(list(range(1,n)))
        while 1:
            i, k = divmod(k, cycle)
            soln.append(numbers[i])
            del numbers[i]
            if not numbers:
                break
            cycle //= len(numbers)
        return "".join(str(i) for i in soln)



def test_1():
    n = 3
    k = 2
    expected = "213"
    assert Solution().solve(n, k) == expected
