"""
binarysearch.com :: Happy Numbers
jramaswami
"""
class Solution:
    def solve(self, n):
        def transform(n):
            return sum(x * x for x in (int(d) for d in str(n)))

        prev = set()
        while n not in prev:
            prev.add(n)
            n = transform(n)
            if n == 1:
                return True
        return False


def test_1():
    assert Solution().solve(7) == True

def test_2():
    assert Solution().solve(11) == False

def test_3():
    assert Solution().solve(986379634) == False
