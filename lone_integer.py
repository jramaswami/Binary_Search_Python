"""
binarysearch.com :: Lone Integer
jramaswami
"""
class Solution:
    def solve(self, nums):
        soln = 0
        for bit in range(33):
            mask = 1 << bit
            set_count = 0
            for n in nums:
                if mask & n:
                    set_count += 1

            if set_count % 3:
                soln = soln | mask

        return soln



def test_1():
    nums = [2, 2, 2, 9, 5, 5, 5]
    assert Solution().solve(nums) == 9


def test_2():
    nums = [7, 1, 1, 1]
    assert Solution().solve(nums) == 7
