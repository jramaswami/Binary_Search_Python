"""
binarysearch.com :: Phone Number Connections
jramaswami
"""


class Solution:

    def solve(self, digits):
        # Special case
        if not digits:
            return []

        letters = [
            '', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'
        ]

        def dfs(i, acc, soln):
            if i >= len(digits):
                soln.append("".join(acc))
                return

            for c in letters[int(digits[i])]:
                acc.append(c)
                dfs(i+1, acc, soln)
                acc.pop()

        soln = []
        dfs(0, [], soln)
        return soln


def test_1():
    digits = "23"
    assert Solution().solve(digits) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
