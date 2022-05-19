"""
binarysearch.com :: Upside Down Numbers
jramaswami
"""


class Solution:

    def solve(self, n):
        soln = []

        def partnered(i, acc):
            partner = n - i - 1
            print(f"partner({i=} {acc=}) {n=} {partner=}")
            if partner >= 0 and partner > i:
                if acc[partner] == '9':
                    return True
                if acc[partner] == '6':
                    return True
            return False

        def get_partner(i, acc):
            partner = n - i - 1
            if partner >= 0:
                if acc[partner] == '9':
                    return '6'
                if acc[partner] == '6':
                    return '9'

        def cannot_be_partner(i):
            if n % 2:
                mid = n // 2
                # print(f"cannot_be_partner({i=}) {mid=}")
                return i == mid
            return False

        def solve0(i, acc):
            if i >= n:
                soln.append("".join(acc))
                return

            if partnered(i, acc):
                # Check and see if we are matching a previous 6 or 9.
                acc.append(get_partner(i, acc))
                solve0(i+1, acc)
                acc.pop()
            else:
                for k in "01689":
                    # print(f"{k=} {cannot_be_partner(i)=}")
                    # No leading zeros.
                    if k == 0 and i == 0:
                        continue
                    if k in "69" and cannot_be_partner(i):
                        continue
                    acc.append(k)
                    solve0(i+1, acc)
                    acc.pop()

        solve0(0, [])
        return soln


def test_1():
    n = 1
    expected = ["0", "1", "8"]
    assert Solution().solve(n) == expected


def test_2():
    n = 2
    expected = ["11", "69", "88", "96"]
    assert Solution().solve(n) == expected
