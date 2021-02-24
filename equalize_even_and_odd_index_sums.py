"""
binarysearch.com :: Equalize Even and Odd Index Sums
jramaswami
"""
class Solution:
    def solve(self, nums):
        odd_suffix = [0 for _ in nums]
        even_suffix = [0 for _ in nums]
        odd_suffix.append(0)
        even_suffix.append(0)

        odd_sum = 0
        even_sum = 0
        for negi, n in enumerate(reversed(nums), start=-(len(nums) - 1)):
            if abs(negi) % 2:
                odd_sum += n
            else:
                even_sum += n
            odd_suffix[-negi] = odd_sum
            even_suffix[-negi] = even_sum

        soln = 0
        odd_sum = 0
        even_sum = 0
        for i, n in enumerate(nums):
            if odd_sum + even_suffix[i+1] == even_sum + odd_suffix[i+1]:
                soln += 1
            if i % 2:
                odd_sum += n
            else:
                even_sum += n
        return soln


def test_1():
    assert Solution().solve([1, 6, 4, 5]) == 1

def test_2():
    assert Solution().solve([1, 1, 0]) == 1

def test_3():
    assert Solution().solve([2, 2, 2]) == 3
