"""
binarysearch.com :: Paying Workers With Coins
jramaswami
"""


class Solution:

    def solve(self, coins, salaries):
        MOD = pow(10, 9) + 7
        coins.sort(reverse=True)
        salaries.sort(reverse=True)
        j = 0
        soln = 1
        for i, salary in enumerate(salaries):
            # Move to a point where all coins to the left can
            # be used to pay current salary.
            while j < len(coins) and coins[j] >= salary:
                j += 1

            # There are j coins that can be used to pay the current
            # salary.  We have already paid i previous employees.
            # So, there are j - i coins left to pay current salary.
            # First, make sure there are enough coins left to pay
            # the current salary.
            if j - i <= 0:
                return 0
            # Pay current salary.
            soln = (soln * (j - i)) % MOD
        return soln


def test_1():
    coins = [1]
    salaries = [2]
    expected = 0
    assert Solution().solve(coins, salaries) == expected


def test_2():
    coins = [1, 2]
    salaries = [2]
    expected = 1
    assert Solution().solve(coins, salaries) == expected


def test_3():
    coins = [1, 2, 3]
    salaries = [1, 2]
    expected = 4
    assert Solution().solve(coins, salaries) == expected
