"""
binarysearch.com :: Unique Characters of Every Substring
jramaswami
"""


import collections


class Solution:

    def solve(self, S):
        MOD = pow(10, 9) + 7

        def count_substrings(unique_target):
            freqs = collections.defaultdict(int)
            window = collections.deque()
            unique_chars = 0
            i = 0
            while i < len(S) and unique_chars < unique_target:
                window.append((S[i], i))
                freqs[S[i]] += 1
                if freqs[S[i]] == 1:
                    unique_chars += 1
                elif freqs[S[i]] > 1:
                    unique_chars -= 1
                i += 1

            # Invariant: window will always satisfy unique_target == unique_chars
            result = 0
            while i < len(S):
                if freqs[S[i]] == 0:
                    # New character.
                    while window and unique_chars == unique_target:
                        # print('substr', window)
                        result = (result + 1) % MOD
                        freqs[window[0][0]] -= 1
                        if freqs[window[0][0]] == 0:
                            unique_chars -= 1
                        # print('popping', window[0])
                        window.popleft()
                        # print(f"{window=} {unique_chars=} {freqs=}")
                    unique_chars += 1
                elif freqs[S[i]] == 1:
                    unique_chars -= 1
                else:
                    # print('substr', window)
                    result = (result + 1) % MOD
                # Add to window.
                freqs[S[i]] += 1
                window.append((S[i], i))
                i += 1

            # print(f"{i=} {window=} {unique_chars=} {freqs=}")
            while window and unique_chars == unique_target:
                # print('substr', window)
                result = (result + 1) % MOD
                freqs[window[0][0]] -= 1
                if freqs[window[0][0]] == 0:
                    unique_chars -= 1
                window.popleft()

            return result


        soln = 0
        # print(S)
        for i in range(1, 27):
            # print('target = ', i)
            k = count_substrings(i)
            t = (k * i) % MOD
            soln = (soln + t) % MOD
        return soln % MOD


def test_1():
    s = "aab"
    expected = 6
    assert Solution().solve(s) == expected
