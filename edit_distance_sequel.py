"""
binarysearch.com :: Edit Distance Sequel
jramaswami
"""


class Solution:

    def solve(self, source, target):

        s = 0
        t = 0
        soln = []
        while s < len(source) or t < len(target):
            # print(f"{s=} {source[s]=} {t=} {target[t]=}")
            if s >= len(source):
                soln.append("+" + target[t])
                t += 1
            elif t >= len(target):
                soln.append("+" + source[s])
                s += 1
            elif source[s] == target[t]:
                soln.append(source[s])
                s += 1
                t += 1
            else:
                # Is there an advantage to inserting in order to avoid deleting later?
                soln.append("-" + source[s])
                s += 1
        return soln




def test_1():
    source = "aab"
    target = "abb"
    expected = ["a", "-a", "b", "+b"]
    result = Solution().solve(source, target)
    assert result == expected


def test_2():
    source = "aaab"
    target = "aabb"
    expected = ["a", "a", "-a", "b", "+b"]
    result = Solution().solve(source, target)
    assert result == expected


def test_3():
    source = "abc"
    target = "cba"
    expected = ["-a", "-b", "c", "+b", "+a"]
    result = Solution().solve(source, target)
    assert result == expected


def test_4():
    source = "bcd"
    target = "acd"
    expected = ["-b", "+a", "c", "c", "d"]
    result = Solution().solve(source, target)
    assert result == expected
