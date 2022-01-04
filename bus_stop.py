"""
binarysearch.com :: bus stop
jramaswami
"""


class Solution:

    def solve(self, nums):
        piles = []

        for n in nums:
            target_pile = len(piles)
            for p, m in enumerate(piles):
                if n > m:
                    target_pile = p
                    break
            if target_pile == len(piles):
                piles.append(n)
            else:
                piles[p] = n
        return len(piles)



def test_1():
    nums = [1, 2, 7, 9, 3, 4]
    assert Solution().solve(nums) == 2


def test_2():
    nums = [5, 5]
    assert Solution().solve(nums) == 2
