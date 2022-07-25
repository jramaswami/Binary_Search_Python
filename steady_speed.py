"""
binarysearch.com :: Steady Speed
jramaswami
"""


class Solution:

    def solve(self, positions):
        # Boundary case:
        if len(positions) < 2:
            return len(positions)
        speeds = [abs(a - b) for a, b in zip(positions[:-1], positions[1:])]
        curr_speed = speeds[0]
        curr_len = 1
        max_len = 0
        for speed in speeds[1:]:
            if speed == curr_speed:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_speed = speed
                curr_len = 1
        max_len = max(max_len, curr_len)
        return max_len + 1


def test_1():
    positions = [0, 3, 6, 3, 0]
    expected = 5
    assert Solution().solve(positions) == expected


def test_2():
    positions = [0, 3, 6, 5, 4, 3, 1, 7, 10, 13]
    expected = 4
    assert Solution().solve(positions) == expected


def test_3():
    positions = []
    expected = 0
    assert Solution().solve(positions) == expected


def test_4():
    positions = [0, 3]
    expected = 2
    assert Solution().solve(positions) == expected


def test_5():
    positions = [3]
    expected = 1
    assert Solution().solve(positions) == expected
