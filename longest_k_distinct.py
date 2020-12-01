"""
binarysearch.com :: Longest Substring with K Distinct Characters
https://binarysearch.com/problems/Longest-Substring-with-K-Distinct-Characters
"""
from collections import defaultdict

class Solution:
    def solve(self, k, s):
        frequency = defaultdict(int)
        distinct = 0
        soln = 0
        left = 0
        for right in range(len(s)):
            # Add the letter at the right pointer
            if frequency[s[right]] == 0:
                distinct += 1
            frequency[s[right]] += 1

            if distinct > k:
                # Move the left pointer if we have exceeded k distinct letters
                while distinct > k:
                    if frequency[s[left]] == 1:
                        distinct -= 1
                    frequency[s[left]] -= 1
                    left += 1

            if distinct <= k:
                soln = max(soln, right - left + 1)

        return soln

def test_1():
    solver = Solution()
    k = 2
    s = "abcba"
    assert solver.solve(k, s) == 3

def test_2():
    solver = Solution()
    k = 1
    s = "aaaaa"
    assert solver.solve(k, s) == 5

def test_3():
    solver = Solution()
    k = 1
    s = "abcde"
    assert solver.solve(k, s) == 1

def test_4():
    solver = Solution()
    k = 58
    s = "o"
    assert solver.solve(k, s) == 1

def test_4():
    solver = Solution()
    k = 79
    s = "}7"
    assert solver.solve(k, s) == 2
