"""
binarysearch.com :: Edit Distance Sequel
jramaswami
"""


import collections


State = collections.namedtuple('State', ['cost', 'parent'])

class Solution:

    def solve(self, source, target):

        del_cost = 1
        ins_cost = 1
        # dp[target][source]
        dp = [[0 for _ in range(len(source) + 1)] for _ in range(len(target) + 1)]
        # Init
        dp[0] = [State(c * ins_cost, (0, c-1)) for c in range(len(source) + 1)]
        for r in range(len(target) + 1):
            dp[r][0] = State(r * del_cost, (r-1, 0))
        dp[0][0] = State(0, None)


        for c in range(1, len(source) + 1):
            s = source[c-1]
            for r in range(1, len(target) + 1):
                t = target[r-1]
                if s == t:
                    dp[r][c] = State(dp[r-1][c-1].cost, (r-1, c-1))
                else:
                    if dp[r-1][c].cost + del_cost <= dp[r][c-1].cost + ins_cost:
                        dp[r][c] = State(dp[r-1][c].cost + del_cost, (r-1, c))
                    else:
                        dp[r][c] = State(dp[r][c-1].cost + ins_cost, (r, c-1))

        for row in dp:
            print(row)

        # posn = (len(target), len(source))
        # path = []
        # while posn:
        #     curr_r, curr_c = posn
        #     path.append(dp[curr_r][curr_c])
        #     posn = dp[curr_r][curr_c].parent

        #     if posn:
        #         next_r, next_c = posn
        #         if curr_r - 1 == next_r and curr_c - 1 == next_c:
        #             soln.append(target[curr_c-1])
        #         elif curr_r - 1 == next_r and curr_c == next_c:
        #             soln.append('-' + target[curr_c-1])
        #         elif curr_r == next_r and curr_c - 1 == next_c:
        #             soln.append('+' + target[curr_c-1])

        # soln = soln[::-1]
        # print(soln)
        # return soln


def test_1():
    source = "aab"
    target = "abb"
    expected = ["a", "-a", "b", "+b"]
    result = Solution().solve(source, target)
    assert result == expected

