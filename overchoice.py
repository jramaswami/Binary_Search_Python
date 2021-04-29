"""
binarysearch.com :: Overchoice
jramaswami
"""
class Solution:
    def solve(self, s):
        i = 0
        soln = [[]]
        while i < len(s):
            if s[i] == "[":
                # Find the end of the bracket
                j = i
                while s[j] != "]":
                    j += 1
                tokens = s[i+1:j].split("|")
                soln0 = []
                for t in tokens:
                    for x in soln:
                        x0 = list(x)
                        x0.append(t)
                        soln0.append(x0)
                soln = soln0
                i = j + 1
            else:
                j = i
                # Find the first bracket
                while j < len(s) and s[j] != "[":
                    j += 1

                for x in soln:
                    x.append(s[i:j])
                i = j

        return ["".join(t) for t in soln]


def test_1():
    s = "[a|b]with[x|y|z]"
    expected = ["awithx", "awithy", "awithz", "bwithx", "bwithy", "bwithz"]
    assert sorted(Solution().solve(s)) == sorted(expected)


def test_2():
    s = "[a|b|c][x|y|z]"
    expected = ["ax", "ay", "az", "bx", "by", "bz", "cx", "cy", "cz"]
    assert sorted(Solution().solve(s)) == sorted(expected)


def test_3():
    s = "[ax|by|cz]"
    expected = ["ax", "by", "cz"]
    assert sorted(Solution().solve(s)) == sorted(expected)


def test_4():
    s = "z"
    expected = ["z"]
    assert sorted(Solution().solve(s)) == sorted(expected)