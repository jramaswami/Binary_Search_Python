"""
binarysearch.com :: H-Index
jramaswami
"""
class Solution:
    def solve(self, citations):
        soln = 0
        if citations:
            citations.sort(reverse=True)
            for have_at_least, h_citations in enumerate(citations, start=1):
                soln = max(soln, min(have_at_least, h_citations))
        return soln


def test_1():
    citations = [4, 3, 0, 1, 5]
    assert Solution().solve(citations) == 3

def test_2():
    citations = [4, 4, 0, 1, 5, 9]
    assert Solution().solve(citations) == 4

def test_3():
    citations = [9, 10, 0, 1, 6]
    assert Solution().solve(citations) == 3

def test_4():
    citations = []
    assert Solution().solve(citations) == 0
