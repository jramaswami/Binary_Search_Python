"""
binarysearch.com :: Number of Islands - Online Version
jramaswami
"""


class Solution:

    OFFSETS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self):
        self.parent = dict()
        self.size = dict()
        self.length = 0

    def make_set(self, key):
        if key not in self.parent:
            self.parent[key] = key
            self.size[key] = 1
            self.length += 1

    def find_set(self, key):
        if self.parent[key] == key:
            return key
        p = self.find_set(self.parent[key])
        self.parent[key] = p
        return p

    def union_set(self, key1, key2):
        key1 = self.find_set(key1)
        key2 = self.find_set(key2)
        if key1 != key2:
            if self.size[key1] < self.size[key2]:
                key1, key2 = key2, key1
            self.parent[key2] = key1
            self.size[key1] += self.size[key2]
            self.length -= 1

    def add_land(self, r, c):
        key = (r, c)
        if key not in self.parent:
            # Insert land.
            self.make_set(key)
            # Join to any existing lands.
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                key0 = (r0, c0)
                if key0 in self.parent:
                    self.union_set(key, key0)

    def solve(self, land_requests):
        soln = []
        for r, c in land_requests:
            self.add_land(r, c)
            soln.append(self.length)
        return soln


def test_1():
    land_requests = [
        [0, 0],
        [1, 1],
        [2, 2],
        [0, 1]
    ]
    expected = [1, 2, 3, 2]
    assert Solution().solve(land_requests) == expected


def xtest_2():
    # Includes duplicate land request.
    land_requests = [[74, 72], [30, 37], [31, 29], [20, 83], [55, 62], [52, 39], [94, 65], [27, 3], [76, 53], [27, 60], [4, 56], [34, 90], [28, 10], [1, 68], [71, 86], [69, 12], [25, 51], [100, 24], [42, 19], [96, 74], [66, 99], [53, 79], [60, 83], [42, 78], [31, 28], [56, 76], [79, 39], [77, 90], [38, 59], [74, 92], [61, 14], [88, 58], [90, 1], [44, 20], [20, 83], [62, 32], [16, 52], [77, 43], [86, 65], [26, 3], [22, 4], [56, 96], [91, 28], [66, 7], [89, 39], [6, 79], [60, 38], [64, 20], [75, 44], [72, 50], [73, 10], [59, 55], [90, 33], [68, 44], [78, 58], [89, 78], [1, 69], [75, 45], [92, 48], [2, 52], [78, 34], [29, 70], [15, 16], [33, 93], [30, 32], [96, 10], [47, 88], [76, 2], [68, 76], [13, 77], [46, 58], [38, 92], [25, 47], [34, 83], [30, 53], [95, 5], [57, 53], [36, 28], [99, 62], [67, 59], [87, 41], [36, 27], [100, 38], [41, 90], [76, 15], [94, 99], [39, 87], [80, 91], [23, 80], [50, 78], [49, 6], [26, 95], [93, 12], [68, 95], [53, 28], [75, 94], [39, 50], [2, 70], [64, 23], [9, 56]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 54, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
    result = Solution().solve(land_requests)
    for ex, rs, lr in zip(expected, result, land_requests):
        if ex == rs:
            print('ex', ex, 'rs', rs, lr)
        else:
            print('ex', ex, 'rs', rs, "***", lr)
    assert result == expected


def main():
    # Timing
    import random
    N = 20
    land_requests = [[a, b] for a, b in set((random.randint(1, N), random.randint(1, N)) for _ in range(200))]
    print(land_requests)
    T = Solution().solve(land_requests)
    print(T)


if __name__ == '__main__':
    main()



