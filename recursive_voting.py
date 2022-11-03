"""
binarysearch.com :: Weekly Contest 40 :: Recursive Voting
jramaswami
"""
from functools import lru_cache

class Solution:

    @lru_cache(maxsize=None)
    def get(self, i):
        if self.votes[i] < 0:
            return 1
        if self.votes[i] >= len(self.votes):
            return 0 

        return self.get(self.votes[i])

    def solve(self, votes):
        self.votes = votes
        return sum(self.get(i) for i in range(len(votes)))


def test_1():
    votes = [2, -1, 5, 1, 3]
    assert Solution().solve(votes) == 3
