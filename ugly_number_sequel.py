"""
binarysearch.com :: Ugly Number Sequel
jramaswami
"""


class Solution:
    def solve(self, n):
        if n == 0:
            return 1
        else:
            ugly_numbers = [1]
            prev_ugly2 = prev_ugly3 = prev_ugly5 = 0
            ugly2 = 2
            ugly3 = 3
            ugly5 = 5
            while len(ugly_numbers) <= n:
                next_ugly = min(ugly2, ugly3, ugly5)
                ugly_numbers.append(next_ugly)
                if next_ugly == ugly2:
                    prev_ugly2 += 1
                    ugly2 = ugly_numbers[prev_ugly2] * 2
                if next_ugly == ugly3:
                    prev_ugly3 += 1
                    ugly3 = ugly_numbers[prev_ugly3] * 3
                if next_ugly == ugly5:
                    prev_ugly5 += 1
                    ugly5 = ugly_numbers[prev_ugly5] * 5
            return ugly_numbers[n]
                

def test_1():
    assert Solution().solve(5) == 6


def test_2():
    assert Solution().solve(100) == 1600
