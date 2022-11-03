"""
binarysearch.com :: Weekly Contest 43 :: Sort List by Reversing Once
jramaswami
"""
class Solution:
    def solve(self, nums):
        if nums == []:
            return True
        nums0 = sorted(nums)
        st = en = -1

        for i, _ in enumerate(nums):
            a = nums[i]
            b = nums0[i]
            if a != b:
                st = i
                break

        for i in range(len(nums) - 1, -1, -1):
            a = nums[i]
            b = nums0[i]
            if a != b:
                en = i + 1
                break

        if st >= 0:
            if en < 0:
                en = len(nums)
            nums[st:en] = reversed(nums[st:en])

        if all(a <= b for a, b in zip(nums[:-1], nums[1:])):
            return True
        return False

        
def test_1():
    nums = [1, 3, 3, 7, 6, 9]
    assert Solution().solve(nums) == True

def test_2():
    nums = [1, 3, 9, 8, 2]
    assert Solution().solve(nums) == False

def test_3():
    nums = [1, 2, 3, 4]
    assert Solution().solve(nums) == True

def test_4():
    nums = []
    assert Solution().solve(nums) == True

def test_5():
    nums = [1, 2, 5, 4, 3]
    assert Solution().solve(nums) == True

def test_6():
    nums = [3, 2, 1, 4, 5]
    assert Solution().solve(nums) == True
