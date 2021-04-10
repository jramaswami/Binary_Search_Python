"""
binarysearch.com :: Team Voting
jramaswami
"""
from collections import defaultdict


class Solution:
    def solve(self, votes):
        vote_totals = defaultdict(lambda: [0 for _ in votes[0]])
        for vote in votes:
            for i, v in enumerate(vote):
                vote_totals[v][i] -= 1

        vote_totals0 = [(v, k) for k, v in vote_totals.items()]
        vote_totals0.sort()
        return "".join(t[1] for t in vote_totals0)



def test_1():
    votes = ["cba", "cab", "abc"]
    assert Solution().solve(votes) == "cab"

def test_2():
    votes = ["ba", "ab"]
    assert Solution().solve(votes) == "ab"

def test_3():
    votes = ["cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc", "cba", "cab", "abc"]
    assert Solution().solve(votes) == "cab"
