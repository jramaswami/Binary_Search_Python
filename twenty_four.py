"""
binarysearch.com :: 24
jramaswami
"""


import operator


class Solution:
    def solve(self, nums):
        ops = [operator.add, operator.sub, operator.mul, lambda a, b: int(a/b)]

        def dfs(nums0):
            # Base Case: only one number.
            if len(nums0) == 1:
                if nums0[-1] == 24:
                    return True
                return False

            for i, _ in enumerate(nums0[:-1]):
                # You can apply operator to nums0[i] and nums0[i+1]
                for op in ops:
                    nums1 = []
                    for j, _ in enumerate(nums0):
                        if j == i:
                            try:
                                nums1.append(op(nums0[j], nums0[j+1]))
                            except:
                                break
                        elif j == i + 1:
                            pass
                        else:
                            nums1.append(nums0[j])

                    if dfs(tuple(nums1)):
                        return True

            return False

        return dfs(tuple(nums))


def test_1():
    nums = [5, 2, 7, 8]
    expected = True
    assert Solution().solve(nums) == expected


def test_2():
    nums = [7, 9, 7, 4]
    expected = True
    assert Solution().solve(nums) == expected


def test_3():
    "WA"
    nums = nums = [4,8,6,0]
    expected = False
    assert Solution().solve(nums) == expected
