"""
binarysearch.com :: List Partitioning
jramaswami
"""


class Solution:
    def solve(self, strs):
        left_boundary = 0
        i = len(strs) - 1
        while i >= 0 and i >= left_boundary:

            # Find rightmost 'red'
            while i >= 0 and strs[i] != 'red':
                i -= 1

            if i >= left_boundary:
                # Swap rightmost red with left boundary.
                strs[left_boundary], strs[i] = strs[i], strs[left_boundary]

                # Move left boundary.
                left_boundary += 1

        # Left boundary now points to first non-Red.  We now repeat process
        # to partition Green and Blue.
        i = len(strs) - 1
        while i >= 0 and i >= left_boundary:

            # Find rightmost Green
            while i >= 0 and strs[i] != 'green':
                i -= 1

            if i >= left_boundary:
                # Swap rightmost green with left boundary.
                strs[left_boundary], strs[i] = strs[i], strs[left_boundary]

                # Move left boundary.
                left_boundary += 1

        return strs


#
# Testing
#


import random


def test_1():
    strs = ["green", "blue", "red", "red"]
    expected = ["red", "red", "green", "blue"]
    result = Solution().solve(strs)
    assert result == expected


def test_2():
    strs = ['red', 'blue', 'red', 'red', 'blue']
    expected = ['red', 'red', 'red', 'blue', 'blue']
    result = Solution().solve(strs)
    assert result == expected


def test_3():
    strs = ['red', 'green', 'green', 'red', 'blue', 'green', 'red', 'red']
    expected = ['red', 'red', 'red', 'red', 'green', 'green', 'green', 'blue']
    result = Solution().solve(strs)
    print(f"{expected=} {result=}")
    assert result == expected


def test_random():
    for _ in range(100):
        strs = []
        for color in ['red', 'green', 'blue']:
            for _ in range(random.randint(0, 1000)):
                strs.append(color)

        expected = list(strs)
        random.shuffle(strs)
        result = Solution().solve(strs)
        print(f"{expected=} {result=}")
        assert result == expected
