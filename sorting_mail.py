"""
binarysearch.com :: Sorting Mail
jramaswami
"""


from collections import deque


class Solution:
    def solve(self, mailboxes):
        # Corner case: empty mailboxes
        if not mailboxes:
            return []

        soln = []

        # Initialize queue
        Q = deque()
        for i, _ in enumerate(mailboxes):
            Q.append((i, 0))

        while Q:
            i, j = Q.popleft()
            if mailboxes[i][j] != 'junk':
                soln.append(mailboxes[i][j])
            if j + 1 < len(mailboxes[i]):
                Q.append((i, j+1))
        return soln


def test_1():
    mailboxes = [
        ["work", "personal"],
        ["junk", "personal", "junk"],
        ["work"]
    ]
    expected = ["work", "work", "personal", "personal"]
    assert Solution().solve(mailboxes) == expected
