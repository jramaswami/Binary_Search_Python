"""
binarysearch.com :: Sum of Four Numbers Less Than Target
jramaswami
"""
from bisect import bisect_right


class Solution:
    def solve(self, A, B, C, D, target):
        # Get every combination of a + b
        AB = [a + b for a in A for b in B]
        # Get every combination of c + d
        CD = [c + d for c in C for d in D]
        # Sort the c + d combinations.
        CD.sort()  
        soln = 0
        # For each possible a + b, use binary search to find the number of
        # c + d such that a + b + c + d <= target.
        for ab in AB:
            k = target - ab
            i = bisect_right(CD, k)
            soln += i
        return soln


def test_1():
    A = [2, 3]
    B = [5, 2]
    C = [0]
    D = [1, 2]
    target = 6
    assert Solution().solve(A, B, C, D, target) == 3


def test_2():
    A = [1, 1]
    B = [0]
    C = [0]
    D = [0]
    target = 1
    assert Solution().solve(A, B, C, D, target) == 2


def test_3():
    """TLE"""
    A = [2, 59, 94, 57, 3, 52, 87, 47, 96, 42, 84, 45, 64, 58, 90, 15, 21, 58, 52, 33, 96, 58, 49, 40, 69, 52, 32, 19, 46, 96, 40, 35, 29, 39, 79, 32, 37, 24, 85, 16, 63, 94, 21, 56, 27, 74, 31, 43, 69, 26, 90, 93, 77, 45, 73, 21, 49, 49, 60, 22, 71, 79, 31, 79, 93, 6, 90, 35, 68, 67, 54, 77, 21, 44, 9, 19, 43, 66, 69, 59, 92, 10, 67, 80, 83, 93, 94, 99, 66, 23, 29, 71, 20, 71, 35, 42, 59, 62, 37, 11, 44, 94, 43, 24, 18, 20, 24, 91, 35, 74, 67, 32, 42, 86, 85, 79, 55, 28, 9, 73, 3, 10, 13, 71, 34, 38, 38, 85, 16, 7, 91, 6, 20, 78, 58, 48, 16, 41, 21, 10, 18, 20, 43, 40, 91, 48, 62, 34, 81, 50, 55, 35, 60, 25, 46, 47, 71, 17, 62, 42, 77, 79, 5, 100, 81, 4, 92, 70, 93, 88, 44, 32, 10, 17, 48, 62, 37, 97, 98, 53, 8, 84, 34, 41, 56, 36, 93, 94, 60, 25, 53, 46, 83, 3, 12, 77, 8, 11, 29, 26, 48, 15, 74, 24, 2, 4, 29, 78, 63, 84, 40, 79, 40, 32, 21, 41, 36, 37, 97, 26, 34, 54, 44, 3, 22, 64, 9, 25, 86, 48, 66, 74, 40, 23, 69, 92, 55, 71, 82, 70, 48, 33, 9, 57, 96, 75, 77, 72, 87, 90, 97, 66, 98, 30, 90, 5, 80, 56, 45, 38, 94, 23, 8, 97, 69, 22, 23, 74, 51, 75, 3, 74, 69, 78, 49, 29, 27, 40, 97, 49, 65, 17, 19, 100, 89, 84, 50, 32, 61, 83, 26, 24, 66, 87, 32, 59, 22, 62, 44, 25, 58, 79, 100, 36, 18, 47, 81, 53, 11, 45, 88, 10, 26, 71, 36, 12, 35, 97, 90, 100, 63, 41, 90, 22, 30, 56, 47, 38, 29, 21, 42, 41, 91, 18, 18, 97, 77, 46, 13, 13, 92, 88, 68, 18, 10, 72, 7, 52, 37, 79, 100, 27, 58, 34, 12, 63, 35, 41, 60, 77, 30, 22, 44, 26, 17, 76, 80, 69, 80, 63, 96, 87, 7, 67, 25, 30, 86, 10, 25, 15, 93, 90, 85, 1, 82, 22, 95, 44, 79, 65, 19, 44, 91, 40, 87, 34, 100, 16, 84, 92]
    B = [11, 25, 93, 23, 47, 34, 18, 39, 89, 73, 90, 80, 77, 42, 33, 16, 77, 62, 68, 60, 16, 21, 48, 10, 5, 48, 42, 99, 48, 27, 88, 43, 88, 70, 62, 40, 70, 17, 51, 36, 35, 49, 1, 44, 56, 99, 63, 56, 31, 79, 13, 73, 86, 6, 8, 63, 89, 93, 94, 19, 42, 3, 82, 37, 79, 85, 95, 47, 77, 42, 93, 24, 40, 21, 71, 23, 43, 2, 27, 38, 97, 17, 92, 94, 27, 3, 66, 44, 2, 57, 18, 64, 55, 94, 88, 87, 99, 84, 49, 96, 26, 99, 97, 51, 69, 58, 53, 61, 38, 58, 100, 2, 86, 77, 66, 82, 13, 78, 57, 19, 68, 80, 27, 31, 57, 83, 71, 15, 53, 3, 67, 12, 90, 21, 99, 74, 76, 15, 70, 40, 11, 69, 79, 87, 16, 21, 9, 98, 28, 54, 74, 31, 40, 11, 72, 16, 15, 23, 89, 79, 4, 31, 18, 19, 7, 40, 99, 98, 86, 50, 55, 86, 20, 92, 40, 16, 15, 27, 25, 46, 77, 52, 31, 54, 5, 5, 56, 7, 47, 29, 13, 11, 90, 89, 65, 50, 75, 67, 50, 76, 51, 18, 8, 22, 31, 93, 9, 70, 74, 63, 40, 25, 73, 59, 70, 12, 58, 51, 66, 76, 19, 81, 93, 16, 24, 22, 61, 36, 16, 74, 73, 16, 39, 56, 10, 47, 93, 70, 97, 89, 5, 43, 34, 89, 34, 39, 77, 55, 30, 15, 86, 8, 60, 65, 45, 42, 27, 61, 22, 83, 41, 62, 91, 84, 22, 21, 91, 35, 20, 73, 94, 74, 61, 46, 38, 70, 3, 92, 51, 45, 38, 67, 72, 3, 9, 35, 33, 21, 2, 48, 32, 99, 87, 21, 45, 39, 98, 14, 100, 89, 50, 28, 31, 20, 55, 15, 11, 93, 92, 26, 19, 59, 19, 29, 23, 63, 74, 11, 88, 70, 15, 6, 23, 53, 43, 42, 83, 61, 58, 100, 38, 7, 36, 26, 59, 75, 77, 19, 98, 10, 53, 39, 4, 13, 29, 12, 26, 65, 94, 43, 83, 48, 22, 34, 84, 16, 5, 17, 17, 33, 98, 89, 63, 63, 48, 10, 58, 87, 68, 80, 48, 80, 36, 14, 20, 78, 69, 22, 94, 84, 68, 18, 62, 5, 29, 49, 20, 35, 83, 5, 28, 47, 24, 51, 89, 77, 81, 39, 41, 58]
    C = [92, 79, 13, 10, 96, 68, 39, 90, 12, 35, 1, 100, 28, 10, 45, 94, 17, 88, 92, 76, 95, 31, 77, 64, 48, 52, 18, 52, 47, 44, 21, 37, 44, 66, 22, 99, 58, 1, 10, 48, 26, 42, 66, 63, 31, 20, 100, 25, 36, 38, 24, 34, 25, 85, 54, 80, 24, 57, 14, 72, 60, 84, 22, 78, 51, 93, 100, 13, 86, 92, 43, 48, 9, 51, 2, 48, 5, 83, 25, 53, 91, 80, 100, 70, 66, 64, 83, 59, 8, 85, 14, 37, 34, 92, 7, 94, 17, 86, 85, 83, 14, 84, 51, 77, 11, 66, 86, 32, 24, 86, 14, 69, 63, 52, 74, 4, 27, 37, 63, 48, 20, 40, 45, 33, 77, 23, 29, 95, 16, 78, 3, 96, 12, 89, 32, 7, 99, 4, 61, 11, 14, 51, 39, 79, 31, 17, 91, 19, 53, 56, 33, 4, 10, 9, 81, 46, 19, 79, 88, 49, 72, 91, 53, 99, 82, 78, 89, 37, 77, 2, 40, 13, 62, 31, 17, 48, 83, 50, 26, 69, 14, 6, 37, 37, 48, 37, 74, 79, 30, 5, 64, 88, 24, 73, 32, 10, 74, 8, 92, 26, 54, 15, 87, 40, 44, 59, 23, 57, 69, 8, 91, 96, 13, 55, 28, 84, 85, 51, 57, 99, 62, 35, 61, 30, 73, 37, 79, 25, 83, 77, 39, 71, 37, 86, 53, 64, 5, 34, 10, 89, 39, 68, 49, 83, 18, 3, 100, 75, 59, 31, 85, 6, 71, 1, 49, 72, 84, 65, 55, 90, 88, 2, 34, 80, 73, 27, 22, 35, 88, 44, 67, 40, 37, 33, 7, 49, 41, 13, 64, 29, 48, 83, 79, 61, 29, 79, 42, 47, 45, 56, 28, 82, 52, 72, 58, 66, 70, 46, 73, 49, 60, 11, 62, 94, 20, 35, 42, 38, 19, 84, 26, 26, 77, 74, 1, 97, 44, 24, 73, 61, 7, 98, 8, 80, 60, 93, 63, 98, 23, 43, 47, 31, 71, 20, 85, 22, 16, 97, 63, 18, 58, 72, 35, 37, 83, 96, 2, 78, 22, 47, 61, 29, 73, 18, 44, 6, 80, 1, 23, 34, 70, 53, 99, 76, 39, 56, 60, 76, 64, 10, 70, 73, 84, 68, 30, 87, 29, 99, 51, 50, 39, 8, 4, 46, 65, 94, 15, 43, 42, 88, 45, 76, 81, 23, 11, 70, 64, 9, 74, 13]
    D = [84, 76, 68, 21, 21, 18, 15, 79, 39, 79, 11, 34, 46, 24, 56, 72, 27, 64, 80, 30, 80, 94, 78, 75, 82, 89, 45, 27, 29, 23, 19, 12, 1, 57, 8, 21, 29, 39, 84, 31, 74, 99, 6, 19, 39, 61, 22, 73, 58, 11, 25, 36, 84, 49, 57, 10, 49, 51, 74, 93, 50, 97, 25, 46, 22, 91, 88, 43, 79, 10, 60, 12, 6, 47, 15, 26, 91, 26, 84, 67, 33, 13, 25, 12, 16, 86, 85, 84, 32, 34, 13, 17, 51, 27, 27, 28, 29, 47, 93, 62, 5, 6, 33, 63, 98, 29, 98, 67, 84, 27, 70, 84, 24, 2, 74, 33, 97, 1, 15, 91, 10, 38, 1, 36, 55, 91, 7, 92, 44, 100, 87, 13, 79, 15, 14, 95, 13, 84, 50, 30, 97, 43, 63, 81, 21, 30, 42, 36, 35, 44, 14, 32, 82, 57, 44, 73, 100, 4, 98, 33, 42, 80, 98, 39, 14, 46, 45, 40, 59, 32, 67, 26, 47, 20, 54, 38, 15, 92, 96, 55, 62, 36, 83, 86, 20, 34, 62, 79, 100, 41, 34, 98, 12, 82, 88, 78, 61, 38, 89, 22, 88, 19, 79, 20, 46, 94, 54, 19, 36, 39, 1, 85, 96, 46, 50, 1, 12, 6, 51, 69, 20, 21, 21, 34, 11, 89, 64, 1, 90, 98, 52, 15, 45, 66, 75, 30, 17, 7, 56, 48, 4, 60, 72, 67, 83, 28, 5, 37, 79, 58, 55, 91, 65, 39, 89, 99, 99, 25, 3, 47, 56, 20, 63, 4, 94, 95, 56, 98, 5, 78, 83, 72, 85, 47, 54, 86, 40, 62, 15, 81, 12, 10, 57, 53, 85, 32, 22, 85, 92, 72, 35, 53, 91, 6, 3, 79, 32, 64, 73, 72, 47, 4, 42, 89, 7, 84, 21, 33, 62, 46, 61, 46, 68, 27, 64, 55, 40, 39, 91, 89, 30, 81, 95, 19, 96, 37, 53, 78, 87, 33, 38, 46, 37, 66, 44, 87, 11, 43, 22, 92, 72, 31, 93, 63, 9, 92, 41, 24, 79, 12, 80, 53, 55, 62, 44, 37, 18, 2, 86, 96, 18, 99, 86, 4, 15, 65, 64, 66, 89, 81, 84, 100, 71, 30, 9, 60, 90, 30, 21, 21, 31, 86, 24, 34, 37, 57, 2, 86, 69, 93, 98, 74, 74, 42, 62, 33, 100, 79, 16, 32]
    target = 100
    assert Solution().solve(A, B, C, D, target) == 950589032
