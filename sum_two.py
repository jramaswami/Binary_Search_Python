"""
binarysearch.com :: Sum of Two Numbers
https://binarysearch.com/problems/Sum-of-Two-Numbers
"""
class Solution:
    def solve(self, nums, k):
        freqs = dict()
        for n in nums:
            if n in freqs:
                freqs[n] += 1
            else:
                freqs[n] = 1

        for n, freq in freqs.items():
            m = k - n
            if m == n and freqs[n] > 1:
                print(m, n)
                return True
            if m != n and m in freqs:
                print(m, n)
                return True
        return False


def test_1():
    solver = Solution()
    nums = [35, 8, 18, 3, 22]
    k = 11
    assert solver.solve(nums, k) == True

def test_2():
    solver = Solution()
    nums = [10, 36, 22, 14]
    k = 4
    assert solver.solve(nums, k) == False

def test_3():
    solver = Solution()
    nums = [24, 10, 11, 4]
    k = 15
    assert solver.solve(nums, k) == True

def test_4():
    solver = Solution()
    nums = [-22, 22, -11, 11]
    k = 0
    assert solver.solve(nums, k) == True

def test_5():
    solver = Solution()
    nums = [15, 0, 3, 2]
    k = 15
    assert solver.solve(nums, k) == True

def test_6():
    solver = Solution()
    nums = [5, 0, 3, 2, 5]
    k = 10
    assert solver.solve(nums, k) == True

def test_7():
    solver = Solution()
    nums = [5, 0, 3, 2]
    k = 10
    assert solver.solve(nums, k) == False

def test_8():
    solver = Solution()
    nums = [2]
    k = 4
    assert solver.solve(nums, k) == False
