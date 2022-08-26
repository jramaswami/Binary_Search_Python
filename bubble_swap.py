"""
binarysearch.com :: Bubble Swap
jramaswami
"""


class Solution:

    def solve(self, lst0, lst1):
        # Find location of each number in lst1.
        locations = {n: i for i, n in enumerate(lst0)}
        swaps = 0
        for i, _ in enumerate(lst1):
            if lst1[i] != lst0[i]:
                # Move element that should be at lst0[i] to that index.
                # Where is the element?
                j = locations[lst1[i]]
                # Move it to it proper index, i.
                while j < i:
                    # Swap right.
                    lst0[j], lst0[j+1] = lst0[j+1], lst0[j]
                    locations[lst0[j]] = j
                    locations[lst0[j+1]] = j+1
                    j += 1
                    swaps += 1
                while j > i:
                    # Swap left
                    lst0[j], lst0[j-1] = lst0[j-1], lst0[j]
                    locations[lst0[j]] = j
                    locations[lst0[j-1]] = j+1
                    j -= 1
                    swaps += 1
        return swaps


def test_1():
    lst0 = [0, 1, 2]
    lst1 = [2, 0, 1]
    expected = 2
    assert Solution().solve(lst0, lst1) == expected


def test_2():
    lst0 = [0, 1, 2]
    lst1 = [2, 1, 0]
    expected = 3
    assert Solution().solve(lst0, lst1) == expected