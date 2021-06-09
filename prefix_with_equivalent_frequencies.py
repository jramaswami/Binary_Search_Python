"""
binarysearch.com :: Prefix with Equivalent Frequencies
jramaswami
"""


from collections import defaultdict


class Solution:
    def solve(self, nums):
        frequency = defaultdict(int)
        frequency_counts = defaultdict(set)
        soln = 0
        for i, n in enumerate(nums):
            if frequency[n]:
                frequency_counts[frequency[n]].remove(n)
                if not frequency_counts[frequency[n]]:
                    del frequency_counts[frequency[n]]
            frequency[n] += 1
            frequency_counts[frequency[n]].add(n)
            if len(frequency_counts) == 2:
                max_key = max(frequency_counts.keys())
                min_key = min(frequency_counts.keys())
                if (min_key + 1 == max_key
                and (len(frequency_counts[max_key]) == 1 
                     or len(frequency_counts[min_key]) == 1)):
                    soln = max(soln, i + 1)
            elif len(frequency_counts) == 1:
                soln = max(soln, i + 1)

        return soln




def test_1():
    nums = [5, 5, 3, 7, 3, 9]
    assert Solution().solve(nums) == 5


def test_2():
    nums = []
    assert Solution().solve(nums) == 0


def test_3():
    nums = [5, -3, 4, -3, -4, -3, -3, 1, 1, 0, -1, 1, 0, -2, -4, -2, -2, 3, 0, 1]
    assert Solution().solve(nums) == 5


def test_4():
    nums = [42 for _ in range(42)]
    assert Solution().solve(nums) == 42


def test_5():
    """WA"""
    nums = [5, 5, 5, 3, 4, 5]
    assert Solution().solve(nums) == 4


def main():
    """Test how long for 100,000 item array."""
    import random
    A = [random.randint(-500, 500) for _ in range(100000)]
    print(Solution().solve(A))


if __name__ == "__main__":
    main()
