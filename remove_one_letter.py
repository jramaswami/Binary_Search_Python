"""
binarysearch.com :: Remove One Letter
jramaswami
"""
class Solution:
    def solve(self, s0, s1):
        """
        Given two strings s0 and s1, return whether you can obtain s1 by 
        removing 1 letter from s0.
        """
        if len(s0) == len(s1) + 1:
            i = 0
            j = 0
            removed = False
            while i < len(s0) and j < len(s1):
                if s0[i] != s1[j]:
                    # If we have already removed a letter from S0, return False
                    if removed:
                        return False
                    # Remove letter from s0 and remember that we did so.
                    # We do this by incrementing the index for s0 without
                    # incrementind the index for s1.
                    i += 1
                    removed = True
                else:
                    # Increment both indices
                    i += 1
                    j += 1
            return True
        else:
            return False


def test_1():
    s0 = "hello"
    s1 = "hello"
    assert Solution().solve(s0, s1) == False


def test_2():
    s0 = "hello"
    s1 = "helo"
    assert Solution().solve(s0, s1) == True


def test_3():
    s0 = "hello"
    s1 = "heloz"
    assert Solution().solve(s0, s1) == False


def test_4():
    s0 = "hello"
    s1 = "hel"
    assert Solution().solve(s0, s1) == False


def test_5():
    s0 = "h"
    s1 = ""
    assert Solution().solve(s0, s1) == True


def test_6():
    s0 = "nnx"
    s1 = "xn"
    assert Solution().solve(s0, s1) == False


def test_7():
    s0 = "aabb"
    s1 = "aba"
    assert Solution().solve(s0, s1) == False
