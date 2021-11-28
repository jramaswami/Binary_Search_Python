"""
binarysearch.com :: No New Friends
jramaswami
"""


class Solution:

    def solve(self, n, friends):
        friend_freqs = [0 for _ in range(n)]
        for a, b in friends:
            friend_freqs[a] += 1
            friend_freqs[b] += 1
        return all(f > 0 for f in friend_freqs)


def test_1():
    n = 3
    friends = [
        [0, 1],
        [1, 2]
    ]
    expected = True
    assert Solution().solve(n, friends) == expected



def test_2():
    n = 3
    friends = [
        [0, 1],
    ]
    expected = False
    assert Solution().solve(n, friends) == expected
