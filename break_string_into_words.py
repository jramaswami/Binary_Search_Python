"""
binarysearch.com :: Break String Into Words
jramaswami

Thank You Larry!
"""


class Solution:

    def solve(self, words, s):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s) + 1):
            if dp[i]:
                for word in words:
                    k = len(word)
                    if s[i:i+k] == word:
                        dp[i+k] = True
        return dp[-1]


def test_1():
    words = ["quick", "brown", "the", "fox"]
    s = "thequickbrownfox"
    assert Solution().solve(words, s) == True


def test_2():
    words = ["hello", "world"]
    s = "hellofoobarworld"
    assert Solution().solve(words, s) == False