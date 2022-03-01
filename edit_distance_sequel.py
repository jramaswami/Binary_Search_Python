"""
binarysearch.com :: Edit Distance Sequel
jramaswami
"""


import math
import collections
import heapq


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
                    # You can delete the character at s.
                    delete = dp[r][c].add_del()
                    if dp[r][c+1] > delete:
                        dp[r][c+1] = delete
                        parent[(r, c+1)] = (r, c)
                    # You can insert the character at t.
                    insert = dp[r][c].add_ins()
                    if dp[r+1][c] > insert:
                        dp[r+1][c] = insert
                        parent[(r+1, c)] = (r, c)

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

        path = []
        curr = (len(dp)-1, len(dp[-1])-1)
        while curr:
            path.append(curr)
            curr = parent[curr]
        path = path[::-1]
        print(path)



        #DEBUG
        print(f"{source=} {target=}")
        for row in dp:
            print(row)

        # # TODO: find shortest path through dp weighted by ops, -dels
        # queue = [(0, 0, 0, 0, None)]
        # while queue:
        #     ops, dels, r, c, p = heapq.heappop(queue)
        #     parent[(r, c)] = p
        #     if r == len(dp) - 1 and c == len(dp[r]) - 1:
        #         break
        #     # Keep
        #     if r+1 < len(dp) and c+1 < len(dp[r]) and dp[r+1][c+1] == ops:
        #         heapq.heappush(queue, (ops, dels, r+1, c+1, (r, c)))
        #     # Delete
        #     if c+1 < len(dp[r]) and dp[r][c+1] < math.inf:
        #         heapq.heappush(queue, (dp[r][c+1], dels+1, r, c+1, (r, c)))
        #     # Insert
        #     if r+1 < len(dp) and dp[r+1][c] < math.inf:
        #         heapq.heappush(queue, (dp[r+1][c], dels, r+1, c, (r, c)))

        # node = (len(dp) - 1, len(dp[-1]) - 1)
        # path = []
        # while node:
        #     path.append(node)
        #     node = parent[node]
        # path = path[::-1]

        # soln = []
        # for left, right in zip(path[:-1], path[1:]):
        #     print(left, right)
        #     if left[0] + 1 == right[0] and left[1] + 1 == right[1]:
        #         soln.append(source[left[1]])
        #     elif left[0] + 1 == right[0]:
        #         soln.append(f"+{target[right[0]]}")
        #     elif left[1] + 1 == right[1]:
        #         soln.append(f"+{source[left[1]]}")
        #     else:
        #         print(f"OOPS {left} {right}")
        # print(soln)

        # r, c = 0, 0
        # soln = []
        # while r + 1 < len(dp) or c + 1 < len(dp[r]):
        #     delete = insert = keep = math.inf
        #     if c + 1 < len(dp[r]):
        #         delete = dp[r][c+1]
        #     if r + 1 < len(dp):
        #         insert = dp[r+1][c]
        #     if r + 1 < len(dp) and c + 1 < len(dp[r]):
        #         keep = dp[r+1][c+1]

        #     print(f"{r=} {c=} {keep=} {delete=} {insert=} {soln=}")
        #     if keep < delete and keep < insert:
        #         # If keep is less than insert/delete, choose it.
        #         soln.append(source[c])
        #         c += 1
        #         r += 1
        #     elif insert < delete:
        #         # If insert is less than delete, choose it.
        #         soln.append(f"+{target[r]}")
        #         r += 1
        #     else:
        #         # Otherwise prefer deletion.
        #         soln.append(f"-{source[c]}")
        #         c += 1

        print(soln)
        return soln

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
#     expected = ["-b", "+a", "c", "d"]
#     result = Solution().solve(source, target)
#     assert result == expected


# def test_5():
#     source = 'gqhdausadyfsozuerncognjgsbazlfbnwyutaxhwbusxpfgpsjpfgqayemzzwbchaamqfyxllsbgbkuevqgkliimruqhkldjonenmtfnwxvjfuofobfwjgmbcsukpfzputjektrafkqfkidnwtwahwqgkznmqftowhpxlcafsnzycphhgknieqrjrnueqmeagmtneecrzljonmuymvsbcacwhqdcxzooyksrthmctjcolkjeivhngctxclbfxldiqjsagamsgmygehhrawonryyrkppptmgamwmxbgeywrlzxktshllneifspcqseditfflozhprlnlhdgtmtzclgxsaxlhayrrzfgrgkzfstaftoewrrtgbsrwmjnlboobgudebvtufjltchewhshlwpnksdkgjnolavujhstmrtgddopixwezsxypebxpqwviricvfngazhealbjjfbfucfrxyktlznyzsgtqslewxcjiakuboxllx'
#     target = 'ehcotggthvxzcwyjgqsisocwwwlamqjfnyfjxzmctgkdswftzytnzhnlnqoyjlrqwiganwwbgdufrbwjkyhydcgqwpwfspglxvsfrphoyznlfuacqvastsjqvwpprjxmgaqphamtkgbuwjbyvvadwuworfhzecydzzlljwmxubrftbfiybsidoxexzqfidxufpgbhtfvggsskwndbiaslrwhehlabscdghjuqhapcecndkfqtjnwuitgydopmarwcxaytrazqhraqstnwoxfjitddgsbkvlbutgxqlamirsfohopjazqktlhzhozboacvtknnnguscydtihechmrelmxwamoroihfxdoogktggmjybmzwahzwvyuzuhwuvethlfspphuhimoousrbjcetarhwmxgnbowdwpncoxehwsrbxjrzcxxxpammtttuohmtgryzqdqefcjyunobivcjpthvqiplzomdwdhafzwqxaamsfovugm'
#     expected = ["-b", "+a", "c", "d"]
#     result = Solution().solve(source, target)
#     assert result == expected
