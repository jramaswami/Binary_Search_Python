"""
binarysearch.com :: Maximize Roster Rating
jramaswami
"""


import math


class Solution:

    def solve(self, ratings, ages):

        ages.sort()

        def solve0(index, min_rating, acc):
            if index >= len(ratings):
                return acc

            # I can skip the player at index.
            without_player = solve0(
                    index + 1,
                    min_rating,
                    acc
            )

            # I can choose the player at index if eligible.
            if ratings[index] < min_rating:
                with_player = solve0(
                        index + 1,
                        ratings[index],
                        acc + ratings[index]
                )
                return max(with_player, without_player)

            return without_player

        return solve0(0, math.inf, 0)


def test_1():
    ratings = [5, 4, 8]
    ages = [25, 24, 18]
    assert Solution().solve(ratings, ages) == 9


def test_2():
    "WA"
    ratings = [1, 1]
    ages = [1, 0]
    assert Solution().solve(ratings, ages) == 2
