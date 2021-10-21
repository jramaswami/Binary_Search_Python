"""
binarysearch.com :: Split String Into Palindromes
jramaswami
"""


import collections


class Solution:

    def solve(self, S):
        # The minimum number of cuts is len(S) - 1.
        dp = collections.defaultdict(lambda: len(S) - 1)
        dp[-1] = -1

        for i, _ in enumerate(S):
            # Keep track of the number of odd frequency letters.  This is
            # done to optimize looking for palindromes since we only need
            # to check if a substring is a palindrome if does not have more
            # than one letter with an odd frequency.
            freqs = collections.defaultdict(int)
            odd_freqs = 0
            for j, c in enumerate(S[i:], start=i):
                freqs[c] += 1
                if freqs[c] % 2:
                    odd_freqs += 1
                else:
                    odd_freqs -= 1

                # If the odd frequency is no more than one, check to see if
                # S[i:j+1] is a palindrome.  If it is, then the minimum number
                # of cuts for the string ending at j is 1 cut for the substring
                # S[i:j+1] added to the minimum number of cuts for the
                # substring ending at i, S[0:i].
                if odd_freqs <= 1 and S[i:j+1] == S[i:j+1][::-1]:
                    dp[j] = min(dp[j], dp[i-1] + 1)

        # We are looking for the number of substrings, so add 1 to the minimum
        # number of cuts.
        return dp[len(S)-1] + 1



def test_1():
    S = "amanaplanacanalpanama"
    expected = 1
    assert Solution().solve(S) == expected


def test_2():
    S = "racecarannakayak"
    expected = 3
    assert Solution().solve(S) == expected


def test_3():
    S = "abc"
    expected = 3
    assert Solution().solve(S) == expected


def test_4():
    S = "atabatab"
    expected = 2
    assert Solution().solve(S) == expected


def test_5():
    S = "a" * 1000
    expected = 1
    assert Solution().solve(S) == expected


def test_6():
    S = "abcde" * 200
    expected = 1000
    assert Solution().solve(S) == expected


def test_7():
    """TLE"""
    S = "xonigqkwqxbnewtzwkunfirmvxdweungwglcwnrcwfsnugqpnjrnxwcqnowcrxgfcpfyyuugbmydmtxnvqjapjaplnfkrjzcmllineilttqrqprvpeostndxcdhtafonwzistyduwpuiappjm"
    expected = 136
    assert Solution().solve(S) == expected
