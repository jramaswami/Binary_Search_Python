"""
binarysearch.com :: Maximize Roster Rating
jramaswami
"""


import math
import collections


Player = collections.namedtuple('Player', ['age', 'rating'])


class Solution:

    def solve(self, ratings, ages):

        players = [Player._make(t) for t in zip(ages, ratings)]
        players.sort()
        print(players)

        def solve0(index, max_rating, acc):
            if index >= len(players):
                return acc

            # I can skip the player at index.
            without_player = solve0(
                    index + 1,
                    max_rating,
                    acc
            )

            # One can choose the player at index if eligible.
            # Since all players picked have age less than candidate player,
            # the candidate player must not have a rating less than any
            # picked player.
            if players[index].rating >= max_rating:
                with_player = solve0(
                        index + 1,
                        players[index].rating,
                        acc + players[index].rating
                )
                return max(with_player, without_player)

            return without_player

        return solve0(0, -math.inf, 0)


def test_1():
    ratings = [5, 4, 8]
    ages = [25, 24, 18]
    assert Solution().solve(ratings, ages) == 9


def test_2():
    "WA"
    ratings = [1, 1]
    ages = [1, 0]
    assert Solution().solve(ratings, ages) == 2
