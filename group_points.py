"""
binarysearch.com :: Group Points
jramaswami
"""
from collections import deque


def euclidean_distance_squared(p1, p2):
    """Return the square of the euclideand distance."""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx * dx) + (dy * dy)


class Solution:
    def solve(self, points, k):
        # Build a graph based on distance.  Compute distance squared to avoid
        # any floating point errors.
        ksq = k * k
        adj = [[] for _ in points]
        for i1, p1 in enumerate(points):
            for i2, p2 in enumerate(points[i1+1:], start=i1+1):
                dsq = euclidean_distance_squared(p1, p2)
                if dsq <= ksq:
                    adj[i1].append(i2)
                    adj[i2].append(i1)
        # BFS to find the number of connected components
        visited = [False for _ in points]
        components = 0
        for root, _ in enumerate(points):
            if not visited[root]:
                components += 1
                visited[root] = True
                queue = deque()
                queue.append(root)
                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        return components


def test_1():
    points = [
        [1, 1],
        [2, 2],
        [3, 3],
        [10, 10],
        [11, 11]
    ]
    k = 2
    assert Solution().solve(points, k) == 2


def test_2():
    """WA"""
    points = [
        [-34, 37],
        [-30, 88]
    ]
    k = 51
    assert Solution().solve(points, k) == 2
