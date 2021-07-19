"""
binarysearch.com :: Fair Pay
jramaswami
"""


class Solution:
    def solve(self, ratings):
        pay = [1 for _ in ratings]
        for r, i in sorted((r, i) for i, r in enumerate(ratings)):
            if i - 1 >= 0 and ratings[i] > ratings[i-1]:
                pay[i] = max(pay[i], pay[i-1] + 1)
            if i + 1 < len(ratings) and ratings[i] > ratings[i+1]:
                pay[i] = max(pay[i], pay[i+1] + 1)
        print(ratings)
        print(pay)
        return sum(pay)


def test_1():
    ratings = [1, 2, 5, 1]
    assert Solution().solve(ratings) == 7
