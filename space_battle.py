"""
binarysearch.com :: Space Battle
jramaswami
"""


class Solution:
    def solve(self, nums):
        soln = []
        for n in nums:
            if n > 0:
                soln.append(n)
            elif n < 0:
                # Remove all rockets that are positive with less mass.
                while soln and soln[-1] > 0 and abs(n) > soln[-1]:
                    soln.pop()

                if soln and -(soln[-1]) == n:
                    # If the remaining rocket has the same mass, remove both
                    # rockets
                    soln.pop()
                elif not soln or soln[-1] < 0:
                    # If the solution is empty or the remaining rockets are
                    # moving left (negative) then add the current rocket.
                    soln.append(n)
                else:
                    # If the remaining rocket is positive and greater than
                    # the current rocket, remove the current rocket.
                    pass
        return soln


def test_1():
    nums = [1, 5, 3, -6]
    assert Solution().solve(nums) == [-6]


def test_2():
    nums = [1, 5, 3, -6, 7]
    assert Solution().solve(nums) == [-6, 7]


def test_3():
    nums = [72, -96, -76, -94, -20, 68, 62, -12, -3, -76, 54, -61, 26, -4, -27, -1, 66, -78, 73, -33]
    expected = [-96, -76, -94, -20, -76, -61, -27, -1, -78, 73]
    assert Solution().solve(nums) == expected


def test_4():
    """WA"""
    nums = [1, -1]
    assert Solution().solve(nums) == []

