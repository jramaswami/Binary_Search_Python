"""
binarysearch.com :: Weekly Contest 41 :: Swap Characters Once to Minimize Differences
jramaswami
"""
from string import ascii_lowercase

class Solution:
    def solve(self, s, t):
        # Count and catalog mismatches
        mismatches = set()
        mismatch_count = 0
        for a, b in zip(s, t):
            if a != b:
                mismatch_count += 1
                mismatches.add(a + b)

        # Can I swap and remove 2?
        for a, b in zip(s, t):
            if a != b:
                if b + a in mismatches:
                    return mismatch_count - 2

        # Can I swap and remove 1?
        for a, b in zip(s, t):
            # Swap ab for b?
            if a != b:
                for c in ascii_lowercase:
                    if a == c or b == c:
                        continue
                    if b + c in mismatches:
                        return mismatch_count - 1

        return mismatch_count


def test_1():
    s = "abbz"
    t = "zcca"
    assert Solution().solve(s, t) == 2

def test_2():
    s = "zfba"
    t = "zbca"
    assert Solution().solve(s, t) == 1

def test_3():
    s = "abc"
    t = "abc"
    assert Solution().solve(s, t) == 0

def test_4():
    s = "abb"
    t = "bac"
    assert Solution().solve(s, t) == 1

def test_5():
    s = "abc"
    t = "bca"
    assert Solution().solve(s, t) == 2
