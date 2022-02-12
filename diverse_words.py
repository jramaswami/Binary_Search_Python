"""
binarysearch.com :: Diverse Words
jramaswami
"""


import collections


class Solution:

    def solve(self, words, k):
        def at_most(n):
            result = 0
            window = collections.deque()
            freqs = collections.defaultdict(int)
            unique_words = 0
            for wd in words:
                window.append(wd)
                freqs[wd] += 1
                if freqs[wd] == 1:
                    unique_words += 1
                while unique_words > n:
                    rm = window.popleft()
                    freqs[rm] -= 1
                    if freqs[rm] == 0:
                        unique_words -= 1

                # Every possible sublist of window has at most n unique words
                result += len(window)
            return result

        return at_most(k) - at_most(k-1)



def test_1():
    words = ["hi", "hello", "hello", "hi"]
    k = 2
    expected = 5
    assert Solution().solve(words, k) == expected
