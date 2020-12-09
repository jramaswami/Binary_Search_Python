"""
binarysearch.com :: Unique Occurrences
https://binarysearch.com/problems/Unique-Occurrences
"""
class Solution:
    def solve(self, nums):
        if nums == []:
            return True

        nums.sort()
        freqs = []
        freq = 1
        prev = nums[0]
        for curr in nums[1:]:
            if prev != curr:
                freqs.append(freq)
                freq = 1
                prev = curr
            else:
                freq += 1
        freqs.append(freq)

        freqs.sort()
        for prev, curr in zip(freqs[:-1], freqs[1:]):
            if prev == curr:
                return False
        return True


def test_1():
    nums = [-3, -1, -1, -1, -2, -2]
    solver = Solution()
    assert solver.solve(nums) == True

def test_2():
    nums = [-3, -1, -1, -1, -2, -2]
    solver = Solution()
    assert solver.solve(nums) == True

def test_3():
    nums = [3, 1, 1, 2, 2, 2, 3]
    solver = Solution()
    assert solver.solve(nums) == False
