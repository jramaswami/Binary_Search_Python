"""
binarysearch.com :: Playlist Count
jramaswami
"""


class Solution:

    def solve(self, num_songs, playlist_size, cycle_length):
        MOD = pow(10, 9) + 7
        # For the indexes i from cycle_length to playlist_size
        # there are num_songs - cycle_length possible songs to choose.
        # Example:
        # 100 songs for a playlist of size 5 with a cycle of 2 is:
        # 100 * 99 * 98 * 98 * 98
        soln = 1
        terms = []
        for i in range(num_songs, num_songs - cycle_length, -1):
            terms.append(i)
            soln = (soln * i) % MOD

        k = num_songs - cycle_length
        t = playlist_size - cycle_length
        terms.extend([k] * t)
        soln = (soln * pow(k, t, MOD)) % MOD
        print(len(terms), terms)
        return soln % MOD



def brute_force(num_songs, playlist_size, cycle_length):
    MOD = pow(10, 9) + 7
    visited = set()

    def solve(acc):
        if len(acc) == playlist_size:
            if tuple(acc) in visited:
                print('dupe', acc)
            else:
                print(acc)
            visited.add(tuple(acc))
            return 1

        result = 0
        for u in range(num_songs):
            if u not in acc[-cycle_length:]:
                acc.append(u)
                result = (result + solve(acc)) % MOD
                acc.pop()
        return result

    acc = []
    return solve(acc)


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


def test_3():
    num_songs = 100
    playlist_size = 100
    cycle_length = 50
    expected = 437918130
    assert Solution().solve(num_songs, playlist_size, cycle_length) == expected


def test_4():
    num_songs = 5
    playlist_size = 5
    cycle_length = 2
    expected = 120
    assert Solution().solve(num_songs, playlist_size, cycle_length) == expected



if __name__ == '__main__':
    num_songs = 5
    playlist_size = 5
    cycle_length = 2
    expected = 120
    soln = brute_force(num_songs, playlist_size, cycle_length)
    print(soln, soln == expected)
