"""
binarysearch.com :: Connect Forest
jramaswami
"""


import collections


class Solution:

    def solve(self, graph):
        # Boundary case:
        if not graph:
            return 0

        # Component id to identify the different disjoint trees.
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
            visited = dict()
            center_node = node1
            queue = collections.deque([(node1, 1), (node2, 2)])
            visited[node1] = 1
            visited[node2] = 2
            while queue:
                node, parent = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in visited:
                        if visited[neighbor] != parent:
                            center_node = node
                            break
                    else:
                        visited[neighbor] = parent
                        queue.append((neighbor, parent))

            return diameter, center_node

        # Find the diameter and center node for each tree in forest.
        diameters = []
        for root, _ in enumerate(graph):
            if comp_id[root] is None:
                diameter, center_node = compute_tree_diameter(root)
                diameters.append((diameter, center_node))

        # Attach the center node of all other trees to the center  node
        # of the tree with the maximum diameter.
        diameters.sort()
        _, center_node0 = diameters[-1]
        for _, center_node in diameters[:-1]:
            graph[center_node0].append(center_node)
            graph[center_node].append(center_node0)

        # Compute the diameter of that tree.  Then subtract one because
        # we are looking for the number of edges not nodes.
        soln, _ = compute_tree_diameter(root)
        return soln - 1


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


def test_4():
    graph = []
    expected = 0
    assert Solution().solve(graph) == expected


def test_5():
    graph = [[]]
    expected = 0
    assert Solution().solve(graph) == expected


def test_6():
    graph = [[], []]
    expected = 1
    assert Solution().solve(graph) == expected