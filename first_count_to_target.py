"""
binarysearch.com :: First Count to Target
jramaswami


The current game state is a winning state if there is a move from the current
state if there is a move that leads to a losing state.

All states greater than or equal to the target are losing states.
"""

WINNING = True
LOSING = False

class Solution:
    def solve(self, k, target):
        is_cached = [False for _ in range(target + 1)]
        cache = [None for _ in range(target + 1)]

        def get(i):
            """Return True if i is a winning state."""
            if i >= target:
                return LOSING
            if not is_cached[i]:
                cache[i] = any(get(j) == LOSING for j in range(i + 1, i + k + 1))
                is_cached[i] = True
            return cache[i]

        return get(0)



def test_1():
    """
    0 1 2 3 4 5 6 7 8 9
    W W W L W W W W W W
    """
    k = 5
    target = 9
    assert Solution().solve(k, target) == True


def test_2():
    """
    0 1 2 3 4
    L W W W W
    """
    k = 3
    target = 4
    assert Solution().solve(k, target) == False
