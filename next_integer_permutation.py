"""
binarysearch.com :: Next Integer Permutation
jramaswami
"""


class Solution:

    def solve(self, N):

        def number_to_list(n):
            digits = []
            while n:
                n, r = divmod(n, 10)
                digits.append(r)
            return digits[::-1]

        def list_to_number(L):
            n = 0
            for d in L:
                n = (n * 10) + d
            return n

        def pandita(L):
            """
            Pandita's algorithm for the next lexicographic permutation.
            REF: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
            """
            # (1) Find the largest index k such that L[k] < L[k + 1].
            # If no such index exists, the permutation is the last permutation.
            k = len(L) - 2
            while k >= 0:
                if L[k] < L[k+1]:
                    break
                k -= 1

            if k == -1:
                return list_to_number(sorted(L))

            # (2) Find the largest index l greater than k such that L[k] < L[l].
            l = len(L) - 1
            while l > k:
                if L[k] < L[l]:
                    break
                l -= 1

            # (3) Swap the value of L[k] with that of L[l].
            L[k], L[l] = L[l], L[k]

            # (4) Reverse the sequence from a[k + 1] up to and including the
            # final element a[n].
            L[k+1:] = L[k+1:][::-1]
            return list_to_number(L)

        return N if N < 10 else pandita(number_to_list(N))


def test_1():
    assert Solution().solve(527) == 572


def test_2():
    assert Solution().solve(321) == 123


def test_3():
    """RTE"""
    assert Solution().solve(0) == 0


def test_4():
    assert Solution().solve(10) == 1


def test_5():
    assert Solution().solve(12) == 21


def test_6():
    assert Solution().solve(123) == 132