"""
binarysearch.com :: Non-Overlapping Pairs of Sublists
jramaswami
"""


import collections


MOD = pow(10, 9) + 7
MOD_INV_2 = 500000004
MOD_INV_24 = 41666667


def S(n):
    # The number of possible sublists for a list of length n.
    result = n
    result *= (n + 1)
    result %= MOD
    result *= MOD_INV_2
    result %= MOD
    return result


def T(n):
    # Sum of i * S(n-i) for i from i to n - 1 if we add 3 to n.
    n += 2
    # Equivalent to n Choose 4.
    result = n
    result *= (n - 1)
    result %= MOD
    result *= (n - 2)
    result %= MOD
    result *= (n - 3)
    result %= MOD
    result *= MOD_INV_24
    result %= MOD
    return result


class Solution:

    def solve(self, nums, k):
        # Determine the number of each length of sublist.
        sublist_freqs = collections.Counter()
        curr = 0
        for n in nums:
            if n >= k:
                curr += 1
            else:
                sublist_freqs[curr] += 1
        sublist_freqs[curr] += 1
        del sublist_freqs[0]
        print(f"{sublist_freqs=}")
        # Count the total number of sublists.
        total_sublists = 0
        for l, f in sublist_freqs.items():
            # A list of length l will have S(l) sublists.
            t = S(l)
            # There are f of those sublists.
            t *= f
            t %= MOD
            total_sublists += t
            total_sublists %= MOD
        print(f"{total_sublists}")
        soln = 0
        for l, f in sublist_freqs.items():
            # How many ways can we split a given sublist into
            # nonoverlapping sublists.
            x = T(l)
            print(f"We can split a sublist of length {l} -> {x}")
            # How many ways can we choose a sublist of our current
            # sublist and pair it with a sublist of another sublist.
            t = S(l)
            s = t * (total_sublists - t)
            s %= MOD
            x += s
            x %= MOD
            # There are f of these lists.
            x *= f
            x %= MOD
            soln += x
            soln %= MOD
        return soln


def test_1():
    nums = [3, 4, 4, 9]
    k = 4
    expected = 57
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [8, 12, 6, 15, 16, 1, 12, 20, 3, 1, 6, 11, 20, 10, 11, 13, 14, 8, 9, 10]
    k = 10
    expected = 262
    assert Solution().solve(nums, k) == expected