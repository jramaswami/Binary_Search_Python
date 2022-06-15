"""
binarysearch.com :: Playlist Count
jramaswami
"""


import collections
import functools


class Solution:

    def solve(self, num_songs, playlist_size, cycle_length):
        MOD = pow(10, 9) + 7

        # dp[length][last cycle_length songs] = count
        prev_dp = collections.defaultdict(int)
        prev_dp[tuple()] = 1
        next_dp = collections.defaultdict(int)
        for p_size in range(1, playlist_size+1):
            for prev_cycle in prev_dp:
                next_cycle = list(prev_cycle[1:]) if len(prev_cycle) > cycle_length else list(prev_cycle)
                for song in range(num_songs):
                    if song not in next_cycle:
                        next_cycle.append(song)
                        key = tuple(next_cycle)
                        next_dp[key] = (next_dp[key] + prev_dp[prev_cycle]) % MOD
                        next_cycle.pop()
            prev_dp, next_dp = next_dp, collections.defaultdict(int)

        soln = 0
        for t in prev_dp.values():
            soln = (soln + t) % MOD
        return soln




def test_1():
    num_songs = 3
    playlist_size = 5
    cycle_length = 2
    expected = 6
    assert Solution().solve(num_songs, playlist_size, cycle_length) == expected


def test_2():
    num_songs = 100
    playlist_size = 5
    cycle_length = 2
    expected = 317800737
    assert Solution().solve(num_songs, playlist_size, cycle_length) == expected

