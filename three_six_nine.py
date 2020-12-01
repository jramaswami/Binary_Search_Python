"""
binarysearch.com :: 3-6-9
https://binarysearch.com/problems/3-6-9
"""

def should_clap(n):
    """ 
    If it's a multiple of 3 or has a 3, 6, or 9 in the number, it should be the
    string 'clap'.
    """
    if n % 3 == 0:
        return True
    else:
        while n:
            n, r = divmod(n, 10)
            if r in [3, 6, 9]:
                return True
    return False


class Solution:
    def solve(self, n):
        return ["clap" if should_clap(i) else str(i) for i in range(1, n+1)]


def test_1():
    solver = Solution()
    assert solver.solve(16) == ["1", "2", "clap", "4", "5", "clap", "7", "8", "clap", "10", "11", "clap", "clap", "14", "clap", "clap"]

