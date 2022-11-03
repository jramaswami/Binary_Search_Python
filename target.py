"""
binarysearch.com :: Number of Sublists That Don't Contain Target List
"""
class Solution:
    def solve(self, nums, target):
        if target == []:
            return 0

        print(nums)
        MOD = pow(10, 9) + 7
        target0 = {k: 0 for k in target}

        soln = 0
        start = 0
        end = -1
        target_numbers_found = 0
        target_sublists = 0

        while start < len(nums):
            # Move forward until we find a spot where there is every number
            # in the sublist
            found_one = False
            while target_numbers_found < len(target) and end + 1 < len(nums):
                # Add the number at end
                end += 1
                v = nums[end]
                if v in target0:
                    if target0[v] == 0:
                        target_numbers_found += 1
                    target0[v] += 1

            if target_numbers_found == len(target):
                # From here to the end every sublist will contain
                # all the target numbers.
                target_sublists = (target_sublists + (len(nums) - end)) % MOD
                found_one = True
            else:
                # If we have reached the end without finding a sublist with
                # all the target numbers, we are done.
                break

            # Move the start forward
            v = nums[start]
            if v in target0:
                if target0[v] == 1:
                    target_numbers_found -= 1
                target0[v] -= 1
            start += 1

        inv2 = pow(2, MOD-2, MOD)
        N = len(nums)
        total_sublists = (N * (N + 1)) % MOD
        total_sublists = (total_sublists * inv2) % MOD
        if total_sublists < 0:
            total_sublists += MOD
        total_sublists -= target_sublists
        if total_sublists < 0:
            total_sublists += MOD

        return total_sublists % MOD


def test_1():
    nums = [1, 2, 2]
    target = [1, 2]
    assert Solution().solve(nums, target) == 4

def test_2():
    nums = [1, 2, 3]
    target = []
    assert Solution().solve(nums, target) == 0

def test_3():
    nums = [3, 0]
    target = [0]
    assert Solution().solve(nums, target) == 1

def test_4():
    nums = [0, 4]
    target = [0]
    assert Solution().solve(nums, target) == 1

def test_5():
    nums = [3, 0, 0]
    target = [0]
    assert Solution().solve(nums, target) == 1
