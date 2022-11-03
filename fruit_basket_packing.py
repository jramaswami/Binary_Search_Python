"""
binarysearch.com :: Fruit Basket Packing
https://binarysearch.com/room/Weekly-Contest-37-u2kU8duwTB?questionsetIndex=2
"""
from collections import namedtuple


Fruit = namedtuple('Fruit', ['basket_remainder', 'cost_to_fill', 'can_fill', 'index'])


class Solution:
    def solve(self, fruits, k, size):
        fruits0 = []

        for i, (fruit_cost, fruit_size, fruit_total) in enumerate(fruits):
            # The fruit must fit in the basket.
            if fruit_size > size:
                continue
            num_to_fill, remainder = divmod(size, fruit_size)
            cost_to_fill = fruit_cost * num_to_fill
            can_fill, remaining_fruits = divmod(fruit_total, num_to_fill)
            # To minimizer remainder first, then cost.
            fruits0.append(Fruit(remainder, cost_to_fill, can_fill, i))
            # Now add the remaining fruits.
            fruits0.append(Fruit(size - (remaining_fruits * fruit_size), remaining_fruits * fruit_cost, 1, i))

        fruits0.sort()
        total_cost = 0
        for _, cost_to_fill, can_fill, i in fruits0:
            baskets_to_fill = min(can_fill, k)
            total_cost += cost_to_fill * baskets_to_fill
            k = k - baskets_to_fill
            if k <= 0:
                break

        return total_cost


def test_1():
    fruits = [
        [4, 2, 3],
        [5, 3, 2],
        [1, 3, 2]
    ]
    k = 2
    size = 4
    solver = Solution()
    assert solver.solve(fruits, k, size) == 9

def test_2():
    fruits = [
        [3, 1, 1]
    ]
    k = 2
    size = 3
    solver = Solution()
    assert solver.solve(fruits, k, size) == 3

def test_3():
    fruits = [
        [2, 3, 2]
    ]
    k = 2
    size = 2
    solver = Solution()
    assert solver.solve(fruits, k, size) == 0