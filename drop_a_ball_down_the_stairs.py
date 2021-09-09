"""
binarysearch.com :: Drop a Ball Down the Stairs
jramaswami
"""


class Solution:

    def solve(self, height, blacklist):
        MOD = pow(10, 9) + 7
        odd_turns = [0 for _ in range(height+1)]
        even_turns = [0 for _ in range(height+1)]
        even_turns[-1] = 1

        blacklist0 = set(blacklist)
        for h in range(height, -1, -1):
            # Do not consider a "death" step.
            if h in blacklist0:
                even_turns[h] = odd_turns[h] = 0
                continue

            for dh in [1, 2, 4]:
                if h - dh >= 0:
                    odd_turns[h - dh] = (odd_turns[h - dh] + even_turns[h]) % MOD

            for dh in [1, 3, 4]:
                if h - dh >= 0:
                    even_turns[h - dh] = (even_turns[h - dh] + odd_turns[h]) % MOD

        return (even_turns[0] + odd_turns[0]) % MOD


def test_1():
    height = 4
    blacklist = [2]
    assert Solution().solve(height, blacklist) == 2


def test_2():
    height = 5
    blacklist = [0]
    assert Solution().solve(height, blacklist) == 0

