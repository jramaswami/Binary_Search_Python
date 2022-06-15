"""
binarysearch.com :: Playlist Count
jramaswami
"""


import collections
import functools


class Solution:

    def solve(self, num_songs, playlist_size, cycle_length):
        MOD = pow(10, 9) + 7

        @functools.cache
        def solve0(T, length):
            # print(f"solve0({T=} {length=})")
            if length == playlist_size:
                return 1

            result = 0
            T0 = collections.deque(T)
            if len(T0) > cycle_length:
                T0.popleft()
            for u in range(num_songs):
                if u in T0:
                    continue
                T0.append(u)
                result = (result + solve0(tuple(T0), length+1)) % MOD
                T0.pop()
            return result % MOD

        return solve0(tuple(), 0)



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

