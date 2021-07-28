"""
binarysearch.com :: Sorting Mail
jramaswami
"""


class Solution:
    def solve(self, mailboxes):
        # Corner case: empty mailboxes
        if not mailboxes:
            return []

        soln = []
        col_limit = max(len(m) for m in mailboxes)
        for c in range(col_limit):
            soln.extend(m[c] for m in mailboxes if c < len(m) and m[c] != 'junk')
        return soln


def test_1():
    mailboxes = [
        ["work", "personal"],
        ["junk", "personal", "junk"],
        ["work"]
    ]
    expected = ["work", "work", "personal", "personal"]
    assert Solution().solve(mailboxes) == expected
