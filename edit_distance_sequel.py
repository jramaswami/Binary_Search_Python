"""
binarysearch.com :: Edit Distance Sequel
jramaswami
"""


import collections


State = collections.namedtuple('State', ['dels', 'inss'])
Posn = collections.namedtuple('Posn', ['row', 'col'])


class Solution:

    def solve(self, source, target):

        def incr_ins(state):
            return State(state.dels, state.inss+1)

        def incr_del(state):
            return State(state.dels+1, state.inss)

        dp = [[State(0, 0) for _ in range(len(source) + 1)]
                           for _ in range(len(target) + 1)]
        dp[0] = [State(c, 0) for c in range(len(source) + 1)]
        for r in range(len(target) + 1):
            dp[r][0] = State(0, r)
        parent = [[None for _ in range(len(source) + 1)]
                        for _ in range(len(target) + 1)]

        for c in range(1, len(target) + 1):
            t = target[c-1]
            for r in range(1, len(source) + 1):
                s = source[c-1]
                if r > c:
                    # Must insert
                    if s == t:
                        parent[r][c] = Posn(r-1, c-1)
                        dp[r][c] = incr_ins(dp[r-1][c-1])
                    else:
                        parent[r][c] = Posn(r-1, c)
                        dp[r][c] = incr_ins(dp[r-1][c])

                elif r <= c:
                    # Must/can delete
                    # Must insert
                    if s == t:
                        parent[r][c] = Posn(r-1, c-1)
                        dp[r][c] = incr_del(dp[r-1][c-1])
                    else:
                        parent[r][c] = Posn(r, c-1)
                        dp[r][c] = incr_del(dp[r][c-1])

        for row in dp:
            print(row)


def test_1():
    source = "aab"
    target = "abb"
    expected = ["a", "-a", "b", "+b"]
    result = Solution().solve(source, target)
    assert result == expected


# def test_2():
#     source = "aaab"
#     target = "aabb"
#     expected = ["a", "a", "-a", "b", "+b"]
#     result = Solution().solve(source, target)
#     assert result == expected


# def test_3():
#     source = "abc"
#     target = "cba"
#     expected = ["-a", "-b", "c", "+b", "+a"]
#     result = Solution().solve(source, target)
#     assert result == expected


# def test_4():
#     source = "bcd"
#     target = "acd"
#     expected = ["-b", "+a", "c", "c", "d"]
#     result = Solution().solve(source, target)
#     assert result == expected
