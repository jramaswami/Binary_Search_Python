"""
binarysearch.com :: Last To Toggle Wins
jramaswami
"""


import functools


class Solution:

    def solve(self, nums):
        init_state = [0 for _ in range(51)]
        curr_sum = 0
        for n in nums:
            if n == 1:
                curr_sum += 1
            else:
                if curr_sum:
                    init_state[curr_sum] += 1
                    curr_sum = 0
        if curr_sum:
            init_state[curr_sum] += 1

        @functools.cache
        def next_states(state):
            "Generate all possible moves from this state."
            result = []
            for i, _ in enumerate(state[:-1]):
                if state[i] == 1 and state[i+1] == 1:
                    state0 = list(state)
                    state0[i] = state0[i+1] = 0
                    result.append(tuple(state0))
            return result

        @functools.cache
        def rec(state):
            # If any of the possible next states are losing states
            # then this is a winning state.
            return (
                False or
                any(rec(s) == False for s in next_states(state))
            )

        return rec(tuple(nums))


def test_1():
    nums = [1, 1, 1, 1]
    expected = True
    assert Solution().solve(nums) == expected


def test_2():
    "WA"
    nums = [1, 1]
    expected = True
    assert Solution().solve(nums) == expected