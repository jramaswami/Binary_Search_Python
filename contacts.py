"""
binarysearch.com :: Weekly Contest 43 :: Unique People in Contact List
jramaswami
"""
class Solution:
    def solve(self, contacts):
        soln = 0
        all_emails = set()
        for emails in contacts:
            if all_emails.isdisjoint(emails):
                soln += 1
            all_emails.update(emails)
        return soln


def test_1():
    contacts = [
        ["elon@tesla.com", "elon@paypal.com"],
        ["elon@tesla.com", "elon@spacex.com"],
        ["tim@apple.com"]
    ]
    assert Solution().solve(contacts) == 2

def test_2():
    contacts = [
        ["bill@microsoft.com"],
        ["jack@twitter.com"],
        ["jeff@amazon.com"]
    ]
    assert Solution().solve(contacts) == 3

def test_3():
    contacts = [
        ["lawrence@gmail.com"],
        ["lawrence@gmail.com", "larry@gmail.com"],
        ["larry@gmail.com"]
    ]
    assert Solution().solve(contacts) == 1
