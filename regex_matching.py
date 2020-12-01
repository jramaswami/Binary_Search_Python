"""
binarysearch.com :: Regular Expression Matching
https://binarysearch.com/problems/Regular-Expression-Matching
"""

def solve0(pptr, sptr, pattern, string):
    """Recursive solution."""
    print('solve0', pptr, sptr, pattern, string)
    if pptr >= len(pattern) and sptr >= len(string):
        return True

    if pptr + 1 < len(pattern) and pattern[pptr+1] == '*':
        print('advance to *')
        return solve0(pptr+1, sptr, pattern, string)

    if pptr < len(pattern) and sptr < len(string) and pattern[pptr] == string[sptr]:
        return solve0(pptr+1, sptr+1, pattern, string)
    
    if pptr < len(pattern) and pattern[pptr] == '.':
        return solve0(pptr+1, sptr+1, pattern, string)

    if pptr < len(pattern) and pattern[pptr] == '*':
        if pattern[pptr-1] == '.':
            # Ignore or consume
            return solve0(pptr+1, sptr, pattern, string) or solve0(pptr, sptr+1, pattern, string)
        else:
            if sptr >= len(string):
                return solve0(pptr+1, sptr, pattern, string)

            if pattern[pptr-1] == string[sptr]:
                # Ignore or consume
                return solve0(pptr+1, sptr, pattern, string) or solve0(pptr, sptr+1, pattern, string)
            else:
                # Must ignore
                return solve0(pptr+1, sptr, pattern, string)

    return False
                

class Solution:
    def solve(self, pattern, s):
        return solve0(0, 0, pattern, s)


def test_1():
    solver = Solution()
    pattern = "ra."
    s = "ray"
    assert solver.solve(pattern, s) == True

def test_2():
    solver = Solution()
    pattern = "a"
    s = "aa"
    assert solver.solve(pattern, s) == False

def test_3():
    solver = Solution()
    pattern = "a*"
    s = "aa"
    assert solver.solve(pattern, s) == True

def test_4():
    solver = Solution()
    pattern = ".*"
    s = "abc"
    assert solver.solve(pattern, s) == True

def test_5():
    solver = Solution()
    pattern = "ac*"
    s = "a"
    assert solver.solve(pattern, s) == True

def test_6():
    solver = Solution()
    pattern = "a*a"
    s = "a"
    assert solver.solve(pattern, s) == True

def test_7():
    solver = Solution()
    pattern = "a*c"
    s = "a"
    assert solver.solve(pattern, s) == False

def test_8():
    solver = Solution()
    pattern = "b*a"
    s = "a"
    assert solver.solve(pattern, s) == True

