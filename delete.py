"""
binarysearch.com :: Weekly Contest 33 :: Unique String Split
"""

def merge_sort(arr, aux, left, right, inversions, nums):
    """
    Merge sort to count the number of items to the left of a given number
    that are less than that number.
    """
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort(arr, aux, left, mid, inversions, nums)
    merge_sort(arr, aux, mid + 1, right, inversions, nums)
    
    left_index = left
    right_index = mid + 1
    aux_index = left_index
    while left_index <= mid and right_index <= right:
        if nums[arr[left_index]] < nums[arr[right_index]]:
            aux[aux_index] = arr[left_index]
            left_index += 1
        else:
            aux[aux_index] = arr[right_index]
            inversions[arr[right_index]] += (left_index - left)
            right_index += 1
        aux_index += 1

    while left_index <= mid:
        aux[aux_index] = arr[left_index]
        left_index += 1
        aux_index += 1

    while right_index <= right:
        aux[aux_index] = arr[right_index]
        inversions[arr[right_index]] += (left_index - left)
        right_index += 1
        aux_index += 1

    for i in range(left, right+1):
        arr[i] = aux[i]


class Solution:
    def solve(self, nums):
        nums0 = list(range(len(nums)))
        inversions = [0 for _ in nums]
        aux = list(nums0)
        merge_sort(nums0, aux, 0, len(nums) - 1, inversions, nums)
        return [i - inversions[i] for i in nums0]



def test_1():
    nums = [3, 5, 1, 4, 2]
    solver = Solution()
    assert solver.solve(nums) == [2, 3, 0, 1, 0]


def test_2():
    nums = []
    solver = Solution()
    assert solver.solve(nums) == []

def test_3():
    nums = list(range(100000))
    solver = Solution()
    assert solver.solve(nums) == [0 for _ in range(100000)]

def test_4():
    nums = list(range(5))
    solver = Solution()
    assert solver.solve(nums) == [0 for _ in range(5)]
