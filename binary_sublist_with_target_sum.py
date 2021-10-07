"""
binarysearch.com :: Binary Sublist with Target Sum
jramaswami
"""


from collections import deque


class Solution:

    def solve(self, nums, target_sum):
        soln = 0
        window = deque()
        curr_sum = 0
        for n in nums:
            if n == 1 and curr_sum == target_sum:
                # Adding the next element will take us over the target sum.
                if target_sum == 0:
                    # If the target sum is zero then any sublist of current
                    # window will sum to 0.
                    soln += ((len(window) * (len(window) + 1)) // 2)
                    # Since the target sum is zero, just empty the window
                    # for the next element.
                    window.clear()
                    curr_sum = 0
                else:
                    # If the target sum is not zero, then we can just count
                    # every window ending at current end if the curr_sum
                    # equals the target_sum
                    while curr_sum == target_sum:
                        soln += 1
                        curr_sum -= window[0]
                        window.popleft()
                    # The curr_sum is now one less than the target sum.
                    # We can add the 1 to get the current sum.
                    window.append(1)
                    curr_sum += 1
            else:
                window.append(n)
                curr_sum += n

        # There still might be items in the window.
        if window and target_sum == curr_sum:
            if target_sum == 0:
                # If the target sum is zero then any sublist of current
                # window will sum to 0.
                soln += ((len(window) * (len(window) + 1)) // 2)
            else:
                # If the target sum is not zero, then we can just count
                # every window ending at current end if the curr_sum
                # equals the target_sum
                while curr_sum == target_sum:
                    soln += 1
                    curr_sum -= window[0]
                    window.popleft()

        return soln


def test_1():
    nums = [1, 0, 1, 1]
    target = 2
    expected = 3
    assert Solution().solve(nums, target) == expected


def test_2():
    """RTE"""
    nums = [1]
    target = 0
    expected = 0
    assert Solution().solve(nums, target) == expected


def test_3():
    nums = [0, 0, 0, 1, 0]
    target = 0
    expected = 7
    assert Solution().solve(nums, target) == expected


def test_4():
    nums = [0, 0, 0, 0, 0]
    target = 0
    expected = 15
    assert Solution().solve(nums, target) == expected


def test_5():
    nums = []
    target = 0
    expected = 0
    assert Solution().solve(nums, target) == expected


def test_6():
    """WA"""
    nums = [0, 0, 0, 1, 0]
    target = 0
    expected = 1
    assert Solution().solve(nums, target) == expected
