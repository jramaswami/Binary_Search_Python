"""
binarysearch.com :: Upside Down Numbers
jramaswami
"""


class Solution:

    def solve(self, n):

        # Boundary case
        if n == 0:
            return []

        soln = []

        def solve0(left, right, acc):
            if left > right:
                soln.append("".join(acc))
                return

            if left == right:
                # Must not be a 6 or 9
                acc[left] = "1"
                solve0(left+1, right-1, acc)
                acc[left] = "8"
                solve0(left+1, right-1, acc)
                acc[left] = "0"
                solve0(left+1, right-1, acc)
            else:
                for k in "018":
                    if left == 0 and k == '0':
                        continue
                    acc[left] = acc[right] = k
                    solve0(left+1, right-1, acc)
                acc[left], acc[right] = '6', '9'
                solve0(left+1, right-1, acc)
                acc[left], acc[right] = '9', '6'
                solve0(left+1, right-1, acc)
                acc[left], acc[right] = '9', '6'

        acc = ["" for _ in range(n)]
        solve0(0, n-1, acc)
        return sorted(soln)


def test_1():
    n = 1
    expected = ["0", "1", "8"]
    assert Solution().solve(n) == expected


def test_2():
    n = 2
    expected = ["11", "69", "88", "96"]
    assert Solution().solve(n) == expected


def test_3():
    n = 3
    expected = ["101", "111", "181", "609", "619", "689", "808", "818", "888", "906", "916", "986"]
    assert Solution().solve(n) == expected
