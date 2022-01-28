"""
binarysearch.com :: Detect Voter Fraud
jramaswami
"""


class Solution:
    def solve(self, votes):
        voted = set()
        for _, voter in votes:
            if voter in voted:
                return True
            voted.add(voter)
        return False
