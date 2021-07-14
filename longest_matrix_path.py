"""
binarysearch.com :: Longest Matrix Path
jramaswami
"""


class Solution:
    def solve(self, matrix):

        dp = [[0 for _ in row] for row in matrix]
        for r, row in enumerate(matrix):


            # Down
            down = [0 for _ in row]
            for c, _ in enumerate(row):
                if r == 0 and matrix[r][c] == 0:
                    down[c] = 1
                elif dp[r-1][c]:
                    down[c] = dp[r-1][c] + 1
                else:
                    down[c] = 0

            # Left to right
            left_to_right = [0 for _ in row]
            for c, _ in enumerate(row):
                if matrix[r][c] == 1:
                    continue
                # My value when moving left to right is the max of my left
                # neighbor or my value coming down.
                from_left = down[c]
                if c-1 >= 0 and left_to_right[c-1]:
                    from_left = left_to_right[c-1] + 1
                left_to_right[c] = max(from_left, down[c])

            # Right
            right_to_left = [0 for _ in row]
            for c in range(len(row) - 1, -1, -1):
                if matrix[r][c] == 1:
                    continue
                # My value when moving right to left is the max of my right
                # neighbor or my value coming down.
                from_right = down[c]
                if c+1 < len(row) and right_to_left[c+1]:
                    from_right = right_to_left[c+1] + 1
                right_to_left[c] = max(from_right, down[c])


            for c, _ in enumerate(row):
                if matrix[r][c] == 1:
                    continue
                dp[r][c] = max(down[c], left_to_right[c], right_to_left[c])

        return max(dp[-1])


def test_1():
    matrix = [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 10


def test_2():
    matrix = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 0


def test_3():
    matrix = [[0]]
    assert Solution().solve(matrix) == 1


def test_4():
    matrix = [[1]]
    assert Solution().solve(matrix) == 0


def test_5():
    matrix = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1]
    ]
    assert Solution().solve(matrix) == 0


def test_6():
    """WA"""
    matrix = [ [1, 0] ]
    assert Solution().solve(matrix) == 1


def main():
    """Main program to test timing."""
    import time
    import random
    # matrix = [[random.randint(0, 1) for _ in range(450)] for _ in range(450)]
    matrix = [[0 for _ in range(450)] for _ in range(450)]
    tic = time.perf_counter()
    print(Solution().solve(matrix))
    toc = time.perf_counter()
    print(f"{toc - tic:0.4f} seconds elapsed")


if __name__ == "__main__":
    main()
