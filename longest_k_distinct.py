"""
binarysearch.com :: Longest Substring with K Distinct Characters
https://binarysearch.com/problems/Longest-Substring-with-K-Distinct-Characters
"""
class Solution:
    def solve(self, k, s):
        frequency = [0 for _ in range(26)]
        distinct = 0
        soln = 0
        left = 0
        ord_a = ord('a')
        for right in range(len(s)):
            # Add the letter at the right pointer
            indexr = ord(s[right]) - ord_a
            if frequency[indexr] == 0:
                distinct += 1
            frequency[indexr] += 1

            if distinct > k:
                # Move the left pointer if we have exceeded k distinct letters
                while distinct > k:
                    indexl = ord(s[left]) - ord_a
                    if frequency[indexl] == 1:
                        distinct -= 1
                    frequency[indexl] -= 1
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
