"""
binarysearch.com :: Triangle Triplets
jramaswami

REF: https://www.geeksforgeeks.org/find-number-of-triangles-possible/
"""


class Solution:

    def solve(self, nums):
        # You cannot have side of length 0.
        nums = sorted(n for n in nums if n > 0)
        soln = 0
        # Fix the side a at index i.
        for i, a in enumerate(nums[:-2]):
            # Initialize side c at index k = i + 2.
            k = i + 2
            # Move side b from indexes i+1 to the end of the array.
            for j, b in enumerate(nums[i+1:], start=i+1):
                # Find the right most element larger than a + b.
                while k < len(nums) and a + b > nums[k]:
                    k += 1
                # If k is more than j then the number of sides that can be c
                # are nums[j+1:k]
                if k > j:
                    soln += (k - j - 1)
        return soln



def test_1():
    nums = [7, 8, 8, 9, 100]
    assert Solution().solve(nums) == 4


def test_2():
    "WA"
    nums = [1, 1, 0]
    assert Solution().solve(nums) == 0


def test_3():
    "WA"
    nums = [2, 1, 1]
    assert Solution().solve(nums) == 0
