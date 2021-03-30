"""
binarysearch.com :: Merging Two Sorted Lists
jramaswami
"""
class Solution:
    def solve(self, a, b):
        soln = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                soln.append(a[i])
                i += 1
            else:
                soln.append(b[j])
                j += 1

        if i < len(a):
            soln.extend(a[i:])

        if j < len(b):
            soln.extend(b[j:])

        return soln


def test_1():
    a = [5, 10, 15]
    b = [3, 8, 9]
    assert Solution().solve(a, b) == [3, 5, 8, 9, 10, 15]

