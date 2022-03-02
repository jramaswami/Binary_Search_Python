"""
binarysearch.com :: Edit Distance Sequel
jramaswami


Will using longest common subsequence help?
"""


import math
import collections
import functools


@functools.total_ordering
class State:

    def __init__(self, ops, dels):
        self.ops = ops
        self.dels = dels

    def add_del(self):
        return State(self.ops+1, self.dels+1)

    def add_ins(self):
        return State(self.ops+1, self.dels)

    def __lt__(self, other):
        if self.ops == other.ops:
            return self.dels < other.dels
        return self.ops < other.ops

    def __eq__(self, other):
        return self.ops == other.ops and self.dels == other.dels

    def __repr__(self):
        return f"{self.ops}/{self.dels}"


class Solution:

    def solve(self, source, target):
        dp = [[State(math.inf, math.inf) for _ in range(len(source)+1)] for _ in range(len(target)+1)]
        dp[0][0] = State(0, 0)
        parent = collections.defaultdict(lambda: None)
        for c, s in enumerate(source):
            for r, t in enumerate(target):
                # Characters are the same, advance both pointers.
                if s == t:
                    dp[r+1][c+1] = min(dp[r+1][c+1], dp[r][c])
                    parent[(r+1, c+1)] = (r, c)
                else:
                    # You can insert the character at t.
                    insert = dp[r][c].add_ins()
                    if dp[r+1][c] > insert:
                        dp[r+1][c] = insert
                        parent[(r+1, c)] = (r, c)
                    # You can delete the character at s.
                    delete = dp[r][c].add_del()
                    if dp[r][c+1] >= delete:
                        dp[r][c+1] = delete
                        parent[(r, c+1)] = (r, c)

        for r, _ in enumerate(target[:-1]):
            insert = dp[r][-1].add_ins()
            if dp[r+1][-1] > insert:
                dp[r+1][-1] = insert
                parent[(r+1, -1)] = (r, -1)
        for c, _ in enumerate(dp[-1][:-1]):
            delete = dp[-1][c].add_del()
            if dp[-1][c+1] > delete:
                dp[-1][c+1] = delete
                parent[(-1, c+1)] = (-1, c)

        # # DEBUG
        print(f"{source=} {target=}")
        for row in dp:
            print(row)

        soln = []
        r, c = len(dp)-1, len(dp[0])-1
        while r - 1 >= 0 or c - 1 >= 0:

            if dp[r][c] == dp[r-1][c-1]:
                print((r,c), '->', (r-1, c-1), soln)  # DEBUG
                soln.append(source[c-1])
                r, c = r-1, c-1
                continue

            insert = State(math.inf, math.inf)
            delete = State(math.inf, math.inf)
            if r-1 >= 0 and c-1 >= 0:
                keep = dp[r-1][c-1]
                if keep != dp[r][c]:
                    keep = State(math.inf, math.inf)
            if r-1 >= 0:
                insert = dp[r-1][c]
            if c-1 >= 0:
                delete = dp[r][c-1]

            print(f"{r=} {c=} {delete=} {insert=}")  # DEBUG

            if delete.ops < insert.ops:
                soln.append(f"-{source[c-1]}")
                print((r,c), '->', (r, c-1), soln)  # DEBUG
                r, c = r, c-1
            else:
                soln.append(f"+{target[r-1]}")
                print((r,c), '->', (r-1, c), soln)  # DEBUG
                r, c = r-1, c
        soln = soln[::-1]
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
    expected = ["-b", "+a", "c", "d"]
    result = Solution().solve(source, target)
    assert result == expected


def test_5():
    "WA"
    source = "aa"
    target= "ba"
    expected = ['-a', '+b', 'a']
    result = Solution().solve(source, target)
    assert result == expected


# def test_x():
#     source = 'gqhdausadyfsozuerncognjgsbazlfbnwyutaxhwbusxpfgpsjpfgqayemzzwbchaamqfyxllsbgbkuevqgkliimruqhkldjonenmtfnwxvjfuofobfwjgmbcsukpfzputjektrafkqfkidnwtwahwqgkznmqftowhpxlcafsnzycphhgknieqrjrnueqmeagmtneecrzljonmuymvsbcacwhqdcxzooyksrthmctjcolkjeivhngctxclbfxldiqjsagamsgmygehhrawonryyrkppptmgamwmxbgeywrlzxktshllneifspcqseditfflozhprlnlhdgtmtzclgxsaxlhayrrzfgrgkzfstaftoewrrtgbsrwmjnlboobgudebvtufjltchewhshlwpnksdkgjnolavujhstmrtgddopixwezsxypebxpqwviricvfngazhealbjjfbfucfrxyktlznyzsgtqslewxcjiakuboxllx'
#     target = 'ehcotggthvxzcwyjgqsisocwwwlamqjfnyfjxzmctgkdswftzytnzhnlnqoyjlrqwiganwwbgdufrbwjkyhydcgqwpwfspglxvsfrphoyznlfuacqvastsjqvwpprjxmgaqphamtkgbuwjbyvvadwuworfhzecydzzlljwmxubrftbfiybsidoxexzqfidxufpgbhtfvggsskwndbiaslrwhehlabscdghjuqhapcecndkfqtjnwuitgydopmarwcxaytrazqhraqstnwoxfjitddgsbkvlbutgxqlamirsfohopjazqktlhzhozboacvtknnnguscydtihechmrelmxwamoroihfxdoogktggmjybmzwahzwvyuzuhwuvethlfspphuhimoousrbjcetarhwmxgnbowdwpncoxehwsrbxjrzcxxxpammtttuohmtgryzqdqefcjyunobivcjpthvqiplzomdwdhafzwqxaamsfovugm'
#     expected = ["-b", "+a", "c", "d"]
#     result = Solution().solve(source, target)
#     assert result == expected
