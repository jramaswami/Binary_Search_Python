"""
binarysearch.com :: Longest Alliteration
jramaswami
"""
class Solution:
    def solve(self, words):
        soln = 0
        current_alliteration = ""
        current_length = 0
        for word in words:
            if word[0] == current_alliteration:
                current_length += 1
            else:
                soln = max(soln, current_length)
                current_alliteration = word[0]
                current_length = 1
        soln = max(soln, current_length)
        return soln


def test_1():
    words = ["she", "sells", "seashells", "he", "sells", "clams"]
    assert Solution().solve(words) == 3

def test_2():
    words = ["alpha", "beta", "gamma", "delta"]
    assert Solution().solve(words) == 1

def test_3():
    words = []
    assert Solution().solve(words) == 0

def test_4():
    words = ["arctomys"]
    assert Solution().solve(words) == 1
