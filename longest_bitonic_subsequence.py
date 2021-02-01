"""
binarysearch.com :: Longest Bitonic Subsequence
jramaswami
"""
class Solution:
    def solve(self, nums):
        queue = []
        new_queue = []
        soln = 1
        for num in nums:
            # You can start here increasing
            t0 = (num, )
            new_queue.append((t0, +1))
            # You can start here decreasing
            new_queue.append((t0, -1))

            for prev_t, prev_dirn in queue:
                # I can just to nothing
                new_queue.append((prev_t, prev_dirn))

                # Can I continue an increasing sequence?
                if prev_dirn == +1 and num > prev_t[-1]:
                    t0 = list(prev_t)
                    t0.append(num)
                    new_queue.append((tuple(t0), +1))

                # Can I change an increasing sequence to a decreasing sequence?
                if prev_dirn == +1 and num < prev_t[-1]:
                    t0 = list(prev_t)
                    t0.append(num)
                    new_queue.append((tuple(t0), -1))
                
                # Can I continue an decreasing sequence?
                if prev_dirn == -1 and num < prev_t[-1]:
                    t0 = list(prev_t)
                    t0.append(num)
                    new_queue.append((tuple(t0), -1))
            queue, new_queue = new_queue, []
        return max((len(t) for t, _ in queue))


def test_1():
    nums = [1, 0, 3, 2, 9, 4, 5, 2]
    assert Solution().solve(nums) == 5

def test_2():
    nums = [10, 2, 5, 7, 3, 1]
    assert Solution().solve(nums) == 5

def test_3():
    nums = [1, 3, 2, 5, 9]
    assert Solution().solve(nums) == 4

def test_4():
    nums = [795, 441, 916, 874, 990, 929, 25, 59, 391, 914, 219, 685, 208, 20, 983, 706, 831, 426, 350, 281, 77, 659, 949, 1019, 360, 271, 777, 453]
    assert Solution().solve(nums) == 10


