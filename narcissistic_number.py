"""
binarysearch.com :: Narcissistic Number
jramaswami
"""
def number_to_list(n):
    digits = []
    while n:
        n, r = divmod(n, 10)
        digits.append(r)
    return digits


class Solution:
    def solve(self, n):
        digits = number_to_list(n)
        return n == sum(pow(d, len(digits)) for d in digits)


def test_1():
    assert Solution().solve(153) == True
