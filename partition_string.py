"""
binarysearch.com :: Partition String
jramaswami
"""


class Solution():
    def solve(self, S):
        # Record the last occurrence of each letter in S
        last_occurrence = {}
        for i, c in enumerate(S):
            last_occurrence[c] = i

        # Partition string
        curr_max = 0
        curr_start = 0
        sizes = []
        for i, c in enumerate(S):
            curr_max = max(last_occurrence[c], curr_max)
            if i == curr_max:
                sizes.append(i - curr_start + 1)
                curr_start = i + 1
        return sizes


def test_1():
    s = "cocoplaydae"
    assert Solution().solve(s) == [4, 1, 1, 4, 1]
