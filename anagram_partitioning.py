"""
binarysearch.com :: Anagram Partitioning
jramaswami
"""


class Solution:
    def solve(self, A, B):
        # Corner case.
        if not A or not B:
            return []

        P = [0 for _ in range(26)]
        Q = [0 for _ in range(26)]

        soln = []
        ord_a = ord('a')
        start = 0
        for i, (a, b) in enumerate(zip(A, B)):
            P[ord(a) - ord_a] += 1
            Q[ord(b) - ord_a] += 1

            if P == Q:
                soln.append(start)
                start = i + 1
                P = [0 for _ in range(26)]
                Q = [0 for _ in range(26)]
        return ([] if sum(P) or sum(Q) else soln)


def test_1():
    a = "catdogwolf"
    b = "actgodflow"
    expected = [0, 2, 3, 6]
    assert Solution().solve(a, b) == expected


def test_2():
    a = "study"
    b = "dusty"
    expected = [0, 4]
    assert Solution().solve(a, b) == expected


def test_3():
    a = ["a"]
    b = ["a"]
    expected = [0]
    assert Solution().solve(a, b) == expected


def test_4():
    a = "aaab"
    b = "caaa"
    expected = []
    assert Solution().solve(a, b) == expected
