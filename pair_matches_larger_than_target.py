"""
binarysearch.com :: Pair Matches Larger Than Target
jramaswami
"""
class Solution:
    def solve(self, nums, target):
        nums0 = sorted(nums)
        right = 1
        soln1 = 0
        for left, b in enumerate(nums0):
            if b is not None:
                for right, a in enumerate(nums0):
                    if left != right and a is not None and b - a >= target:
                        soln1 += 1
                        nums0[right] = None
                        nums0[left] = None
                        break

        nums0 = sorted(nums, reverse=True)
        right = 1
        soln2 = 0
        for left, b in enumerate(nums0):
            if b is not None:
                for right, a in enumerate(nums0):
                    if left != right and a is not None and abs(b - a) >= target:
                        soln2 += 1
                        nums0[right] = None
                        nums0[left] = None
                        break

        return max(soln1, soln2)



def test_1():
    nums = [1, 3, 5, 9, 10]
    target = 3
    assert Solution().solve(nums, target) == 2


def test_2():
    """WA"""
    nums = [0, 1, 2, 3]
    target = 3
    assert Solution().solve(nums, target) == 1


def test_3():
    """WA"""
    nums = [0, 1, 2, 2]
    target = 1
    assert Solution().solve(nums, target) == 2


def test_4():
    """WA"""
    nums = [1, 1, 2, 2, 3, 3]
    target = 1
    assert Solution().solve(nums, target) == 3
