"""
binarysearch.com :: Playlist Count
jramaswami
"""


class Solution:

    def solve(self, num_songs, playlist_size, cycle_length):
        # dp[length of playlist][unique songs] = number of ways to get this playlist
        # For any playlist there are min(cycle_length, length of playlist)
        # songs that we *cannot* add for the next state because they would
        # cause a cycle.

        MOD = pow(10, 9) + 7
        dp = [[0 for _ in range(num_songs+1)] for _ in range(playlist_size+1)]
        dp[0][0] = 1    # There is one empty playlist.
        soln = 0
        for p, _ in enumerate(dp[:-1]):
            for u, _ in enumerate(dp[p]):
                if dp[p][u]:
                    excluded = min(cycle_length, p)
                    useable = num_songs - excluded
                    first_timers = num_songs - u
                    repeats = useable - first_timers
                    # First timers will add to the number of unique songs.
                    if first_timers > 0:
                        k = (dp[p][u] * first_timers) % MOD
                        dp[p+1][u+1] = (dp[p+1][u+1] + k) % MOD
                    # Repeats will not add to the number of unique songs.
                    if repeats > 0:
                        k = (dp[p][u] * repeats) % MOD
                        dp[p+1][u] = (dp[p+1][u] + k) % MOD

        return dp[-1][num_songs] % MOD


def test_1():
    num_songs = 3
    playlist_size = 5
    cycle_length = 2
    expected = 6
    assert Solution().solve(num_songs, playlist_size, cycle_length) == expected


def test_2():
    num_songs = 5
    playlist_size = 5
    cycle_length = 2
    expected = 120
    assert Solution().solve(num_songs, playlist_size, cycle_length) == expected


def test_3():
    num_songs = 100
    playlist_size = 100
    cycle_length = 50
    expected = 437918130
    assert Solution().solve(num_songs, playlist_size, cycle_length) == expected


def test_4():
    num_songs = 5
    playlist_size = 10
    cycle_length = 2
    expected = 115920
    assert Solution().solve(num_songs, playlist_size, cycle_length) == expected


def test_5():
    num_songs = 50
    playlist_size = 100
    cycle_length = 2
    expected = 927191191
    assert Solution().solve(num_songs, playlist_size, cycle_length) == expected
