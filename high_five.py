"""
binarysearch.com :: High Five
jramaswami
"""


def number_to_list(n):
    digits = []
    while n:
        n, r = divmod(n, 10)
        digits.append(r)
    return list(reversed(digits))


def digits_to_number(digits):
    n = 0
    m = 1
    for d in digits[::-1]:
        n += (m * d)
        m *= 10
    return n


class Solution:
    def solve(self, n):
        digits = number_to_list(abs(n))
        result = []
        if n < 0:
            for i, d in enumerate(digits):
                if d > 5:
                    result.append(5)
                    result.extend(digits[i:])
                    break
                else:
                    result.append(d)
        else:
            for i, d in enumerate(digits):
                if d < 5:
                    result.append(5)
                    result.extend(digits[i:])
                    break
                else:
                    result.append(d)

        if len(result) < len(digits) + 1:
            result.append(5)

        soln = digits_to_number(result)
        if n < 0:
            soln *= -1
        return soln


def test_1():
    assert Solution().solve(923) == 9523


def test_2():
    assert Solution().solve(-234) == -2345


def test_3():
    assert Solution().solve(1) == 51