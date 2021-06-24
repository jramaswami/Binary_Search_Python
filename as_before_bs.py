"""
binarysearch.com :: As Before Bs
jramaswami
"""


class Solution:
    def solve(self, s):
        # Corner case: empty string.
        if not s:
            return 0

        # Compute the number of B's before a given index.
        # This is done in O(N) time.
        bs_before = [0 for _ in s]
        curr = 0
        for i, c in enumerate(s):
            bs_before[i] = curr
            if c == "B":
                curr += 1

        # Compute the number of A's after a given index
        # This is done in O(N) time.
        as_after = [0 for _ in s]
        curr = 0
        for i, c in enumerate(reversed(s), start=1):
            as_after[-i] = curr
            if c == "A":
                curr += 1

        # Consider the dividing line at any given index.
        # At that index we must remove all B's before that index and all A's
        # after that index to meet the constraint of A's before B's.  Given
        # the sums we have computed above, we can find the index where the sum
        # of the A's removed and B's removed is minimized.
        # This is done in O(N) time.
        # The overall time complexity is  3 * O(N) which is O(N).
        return min(a + b for a, b in zip(as_after, bs_before))


def test_1():
    s = "AABBAB"
    expected = 1
    assert Solution().solve(s) == expected


def test_2():
    s = ""
    expected = 0
    assert Solution().solve(s) == expected
