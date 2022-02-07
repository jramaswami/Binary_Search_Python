"""
binarysearch.com :: IP Address Combinations
jramaswami
"""


class Solution:

    def solve(self, ip):

        boundaries = [0, None, None, None, None]
        acc = []

        def valid_boundary(left, right):
            "Return True if boundary is valid."
            if left >= len(ip) or right > len(ip):
                return False
            if ip[left] == '0' and left + 1 != right:
                return False
            if 0 <= int(ip[left:right]) <= 255:
                return True
            return False

        def make_ip_address():
            "Return ip address as string given the current boundaries."
            a, b, c, d, e = boundaries
            return f"{ip[a:b]}.{ip[b:c]}.{ip[c:d]}.{ip[d:e]}"

        def solve0(bindex):
            "Recursive solution."
            if bindex == 4:
                if valid_boundary(boundaries[3], len(ip)):
                    boundaries[-1] = len(ip)
                    acc.append(make_ip_address())
                    boundaries[-1] = None
                return

            # Length can be up to three characters.
            left = boundaries[bindex-1]
            for offset in range(1, 4):
                right = left + offset
                if valid_boundary(left, right):
                    boundaries[bindex] = right
                    solve0(bindex+1)
                    boundaries[bindex] = None

        solve0(1)
        return acc


def test_1():
    ip = "2542540123"
    expected = ["254.25.40.123", "254.254.0.123"]
    result = Solution().solve(ip)
    assert sorted(result) == sorted(expected)
