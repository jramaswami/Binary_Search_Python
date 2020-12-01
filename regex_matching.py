"""
binarysearch.com :: Regular Expression Matching
https://binarysearch.com/problems/Regular-Expression-Matching
"""
class Solution:
    def solve(self, pattern, s):
        pattern_ptr = 0
        string_ptr = 0
        # TODO: Backtracking is necessary
        while pattern_ptr < len(pattern):
            if pattern[pattern_ptr] == '.'  and pattern_ptr + 1 < len(pattern) and pattern[pattern_ptr+1] == '*':
                # This will match to the end of the string.
                return True
            if pattern_ptr + 1 < len(pattern) and pattern[pattern_ptr+1] == '*':
                # If you found one, advance the string pointer until there are
                # no more of the char.
                while string_ptr < len(s) and s[string_ptr] == pattern[pattern_ptr]:
                    string_ptr += 1
                # Now advance the pattern_ptr past the '*'
                pattern_ptr += 2
            elif pattern[pattern_ptr] == '.':
                # The '.' matches anything, advance both pointers.
                if string_ptr >= len(s):
                    return False
                pattern_ptr += 1
                string_ptr += 1
            else:
                # This is a regular character and must match.
                if string_ptr >= len(s):
                    return False
                if pattern[pattern_ptr] != s[string_ptr]:
                    return False
                #If there is a match, advance both pointers.
                pattern_ptr += 1
                string_ptr += 1
        # At the end, you must have matched all characters from pattern
        # and string, so both points must be at the len.
        return pattern_ptr == len(pattern) and string_ptr == len(s)


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
