"""
binarysearch.com :: Reverse Sublists to Convert to Target
jramaswami
"""
class Solution:
    def solve(self, nums, target):
        print(nums)
        print(target)
        i = 0
        while i < len(nums) and i < len(target):
            # If they nums[i] and target[i] do not match, find nums[i]
            # in target[i] and reverse the array between the two.
            if nums[i] != target[i]:
                print('mismatch @', i, nums[i], target[i], 'looking for', nums[i])
                j = i
                while j < len(target) and target[j] != nums[i]:
                    j += 1
                nums[i:j+1] = reversed(nums[i:j+1])
                print(f"reversed [{i}:{j+1}], {nums}")
                i = j + 1
            else:
                i += 1
        print(nums)
        print(target)
        return nums == target


def test_1():
    nums = [1, 2, 3, 8, 9]
    target = [3, 2, 1, 9, 8]
    assert Solution().solve(nums, target) == True

def test_2():
    nums = [10, 2, 3, 8, 9]
    target = [3, 2, 1, 9, 8]
    assert Solution().solve(nums, target) == False

def test_3():
    nums = [3, 4, 5, 5]
    target = [3, 4, 5]
    assert Solution().solve(nums, target) == False

def test_4():
    nums = [5, 3, 2, 3, 0]
    target = [5, 0, 3, 2, 3]
    assert Solution().solve(nums, target) == True
