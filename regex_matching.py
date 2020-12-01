"""
binarysearch.com :: Regular Expression Matching
https://binarysearch.com/problems/Regular-Expression-Matching
"""
def solve_recursive(pptr, sptr, pattern, text):
    """Recursive solution."""
    if pptr >= len(pattern) and sptr >= len(text):
        return True

    if pptr + 1 < len(pattern) and pattern[pptr+1] == '*':
        return solve0(pptr+1, sptr, pattern, text)

    if pptr < len(pattern) and sptr < len(text) and pattern[pptr] == text[sptr]:
        return solve0(pptr+1, sptr+1, pattern, text)
    
    if sptr < len(text) and pptr < len(pattern) and pattern[pptr] == '.':
        return solve0(pptr+1, sptr+1, pattern, text)

    if pptr < len(pattern) and pattern[pptr] == '*':
        # Is this the end of the text?
        if sptr >= len(text):
            return solve0(pptr+1, sptr, pattern, text)

        if pattern[pptr-1] == '.':
            # Ignore or consume
            return solve0(pptr+1, sptr, pattern, text) or solve0(pptr, sptr+1, pattern, text)
        else:
            if pattern[pptr-1] == text[sptr]:
                # Ignore or consume
                return solve0(pptr+1, sptr, pattern, text) or solve0(pptr, sptr+1, pattern, text)
            else:
                # Must ignore
                return solve0(pptr+1, sptr, pattern, text)

    return False
                

def solve_dp(pattern, text):
    """Solve using dynamic programming."""
    dp = [[False for _ in range(len(pattern)+1)] for _ in range(len(text)+1)]
    dp[0][0] = True

    # Handle any wildcards that make a zero text match.
    for i in range(1, len(pattern)+1):
        if pattern[i-1] == '*':
            dp[0][i] = dp[0][i-2]

    # Use dynamic programming to solve
    for i in range(1, len(text)+1):
        for j in range(1, len(pattern)+1):
            # Direct match
            if pattern[j-1] == '.' or pattern[j-1] == text[i-1]:
                dp[i][j] = dp[i-1][j-1]
            # Multimatch
            elif pattern[j-1] == '*':
                # We could have zero occurrences of the quantified.
                dp[i][j] = dp[i][j-2]
                # Or we could have multiple occurrences of the quantified.
                if pattern[j-2] == '.' or pattern[j-2] == text[i-1]:
                    dp[i][j] = (dp[i][j] or dp[i-1][j])
            else:
                dp[i][j] = False
    return dp[-1][-1]


class Solution:
    def solve(self, pattern, s):
        return solve_dp(pattern, s)


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

def test_9():
    solver = Solution()
    pattern = ".*c"
    s = "ab"
    assert solver.solve(pattern, s) == False

def test_10():
    solver = Solution()
    pattern = "......."
    s = "abcd"
    assert solver.solve(pattern, s) == False

def test_11():
    solver = Solution()
    pattern = "a*a*a*a*a*a*a*a*a*a*c"
    s = "aaaaaaaaaaaaab"
    assert solver.solve(pattern, s) == False
