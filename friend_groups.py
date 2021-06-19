"""
binarysearch.com :: Friend Groups
jramaswami
"""

from collections import deque


class Solution:
    def solve(self, friends):
        # We can use graph traversal to solve this.
        visited = set()
        soln = 0
        for start, _ in enumerate(friends):
            if start not in visited:
                soln += 1
                queue = deque([start])
                visited.add(start)
                while queue:
                    node = queue.popleft()
                    for neighbor in friends[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return soln


def test_1():
    friends = [
        [1],
        [0, 2],
        [1],
        [4],
        [3],
        []
    ]
    assert Solution().solve(friends) == 3
