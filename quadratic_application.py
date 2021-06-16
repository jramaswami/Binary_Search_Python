"""
binarysearch.com :: Quadratic Application
jramaswami
"""


from collections import deque


class Solution:
    """
    You are given a list of integers nums sorted in ascending order, and
    integers a, b, and c. Apply the following function for each number x in
    nums: ax^2+bx+c and return the resulting list in ascending order.

    This should be done in O(n) time.
    """

    def solve(self, nums, a, b, c):
        """Solve problem."""
        # Base case
        if not nums:
            return nums

        def f(x):
            """Return f(x) = ax^2 + bx + c"""
            return (a * x * x) + (b * x) + c

        nums0 = deque(f(x) for x in nums)
        soln = []

        # Determine which way is up.
        if a <= 0:
            # If a is negative, the parabola faces down.  The smaller values
            # are at the end.
            # Merge inwards.
            while nums0:
                if nums0[0] < nums0[-1]:
                    soln.append(nums0[0])
                    nums0.popleft()
                else:
                    soln.append(nums0[-1])
                    nums0.pop()
        else:
            # If a is positive, the parabola faces up.  The smaller values
            # are in the middle.

            # Find the valley
            _, left = min((x, i) for i, x in enumerate(nums0))
            right = left + 1

            # Merge outwards.
            while len(soln) < len(nums0):
                if left < 0:
                    soln.append(nums0[right])
                    right += 1
                elif right >= len(nums0):
                    soln.append(nums0[left])
                    left -= 1
                elif nums0[left] < nums0[right]:
                    soln.append(nums0[left])
                    left -= 1
                else:
                    soln.append(nums0[right])
                    right += 1
        return soln


#
# Testing
#
import random


def brute_force(nums, a, b, c):
    """N log N solution using sorting."""
    return sorted((a * x * x) + (b * x) + c for x in nums)


def test_1():
    nums = [-2, 3]
    a = 1
    b = -3
    c = 2
    expected = [2, 12]
    assert Solution().solve(nums, a, b, c) == expected


def test_2():
    nums = [-10, -9, -7, -6, -6, -6, -5, 6, 7, 10]
    a = 6
    b = -3
    c = 0
    expected = brute_force(nums, a, b, c)
    result = Solution().solve(nums, a, b, c)
    assert result == expected


def test_random_small():
    T = 1000
    K = 1000
    N = 1000
    for _ in range(T):
        nums = sorted(random.randint(-K, K) for _ in range(N))
        a = random.randint(-K, K)
        b = random.randint(-K, K)
        c = random.randint(-K, K)
        print(f"{nums=} {a=} {b=} {c=}")
        expected = brute_force(nums, a, b, c)
        result = Solution().solve(nums, a, b, c)
        assert result == expected


def test_random_large():
    T = 1
    K = pow(10, 6)
    N = pow(10, 6)
    for _ in range(T):
        nums = sorted(random.randint(-K, K) for _ in range(N))
        a = random.randint(-K, K)
        b = random.randint(-K, K)
        c = random.randint(-K, K)
        print(f"{nums=} {a=} {b=} {c=}")
        expected = brute_force(nums, a, b, c)
        result = Solution().solve(nums, a, b, c)
        assert result == expected
