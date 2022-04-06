"""
binarysearch.com :: Sum of Three Numbers Sequel
jramaswami
"""


def find_rightmost_equal(lo, hi, target, nums):
    k = -1
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        if nums[mid] == target:
            k = max(k, mid)
            lo = mid + 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return k


def find_rightmost_less(lo, hi, target, nums):
    k = -1
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        if nums[mid] == target:
            lo = mid + 1
        elif nums[mid] < target:
            k = max(k, mid)
            lo = mid + 1
        else:
            hi = mid - 1
    return k


def find_leftmost_greater(lo, hi, target, nums):
    k = len(nums)
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        if nums[mid] == target:
            lo = mid + 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            k = min(k, mid)
            hi = mid - 1
    return k


class Solution:
    def solve(self, nums, target):
        nums.sort()
        leftmost = collections.defaultdict(math.inf)
        rightmost = collections.defaultdict(-math.inf)
        for i, n in enumerate(nums):
            leftmost[n] = min(leftmost[n], i)
            rightmost[n] = max(rightmost[n], i)

        soln = abs(target - (sum(nums[:3])))
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:], start=i+1):
                d = target - n - m
                eqi = find_rightmost_equal(j+1, len(nums)-1, d, nums)
                if eqi > j:
                    soln = min(soln, abs(target - (n + m + nums[eqi])))
                lti = find_rightmost_less(j+1, len(nums)-1, d, nums)
                if lti > j:
                    soln = min(soln, abs(target - (n + m + nums[lti])))
                gti = find_leftmost_greater(j+1, len(nums)-1, d, nums)
                if gti < len(nums) and gti > j:
                    soln = min(soln, abs(target - (n + m + nums[gti])))
        return soln


def test_1():
    nums = [2, 4, 25, 7]
    k = 15
    expected = 2
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [2, 4, 25, 7]
    k = 0
    expected = 13
    assert Solution().solve(nums, k) == expected


def test_3():
    "WA"
    nums = [1,-1,0,-2]
    k = 0
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_4():
    "WA"
    nums = [1,-1,1,-2]
    k = 0
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_5():
    "WA"
    nums = [1,-2,-2,1]
    k = -1
    expected = 1
    assert Solution().solve(nums, k) == expected
