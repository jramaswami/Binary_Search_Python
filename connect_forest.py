"""
binarysearch.com :: Connect Forest
jramaswami
"""


import collections
import heapq


class Solution:

    def solve(self, graph):
        comp_id = [None for _ in graph]

        def compute_tree_diameter(root):
            "Returns diameter and center node of tree."
            # BFS to find the farthest node from root, call it node1.
            queue = collections.deque([root])
            node1 = None
            visited = set()
            visited.add(root)
            while queue:
                node1 = node = queue.popleft()
                comp_id[node] = root
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            # BFS to find the distance between node1 and the farthest node
            # from node1.  This is the diameter of the tree.
            diameter = 0
            node2 = None
            queue = collections.deque([(node1, 1)])
            visited = set()
            visited.add(node1)
            while queue:
                node, dist = queue.popleft()
                if dist > diameter:
                    diameter, node2 = dist, node
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist+1))
            # BFS to find the center node.
            visited = collections.defaultdict(int)
            center_node = None
            queue = collections.deque([(node1

            return diameter

        diameters = []
        for root, _ in enumerate(graph):
            if comp_id[root] is None:
                diameter = compute_tree_diameter(root)
                heapq.heappush(diameters, diameter)
                while len(diameters) > 2:
                    heapq.heappop(diameters)

        if len(diameters) == 2:
            a, b = diameters
            return (a // 2) + (b // 2) + 1
        return diameters[0] - 1


def test_1():
    graph = [
        [1, 2],
        [0],
        [0, 3],
        [2],
        [5],
        [4]
    ]
    expected = 4
    assert Solution().solve(graph) == expected


def test_2():
    graph = [
        [1, 4],
        [0, 2, 3],
        [1],
        [1],
        [0]
    ]
    expected = 3
    assert Solution().solve(graph) == expected


def test_3():
    "WA"
    graph = [[], [], [], []]
    expected = 2
    assert Solution().solve(graph) == expected