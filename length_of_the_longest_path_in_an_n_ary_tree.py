"""
binarysearch.com :: Length of the Longest Path in an N-Ary Tree
jramaswami
"""
from collections import defaultdict, deque
from heapq import nlargest

# For any given node the longest path in the tree rooted at that node is:
# (1) 1 if the node has no children.
# (2) The longest path to a leaf node in the tree if the node has
#     one child.
# (3) The sum of the longest two paths to a leaf node for all of the
#     children + 1 for the root node.

def solve0(node, adj):
    """Recursive solution."""
    number_of_children = len(adj[node])
    if number_of_children == 0:
        return 1, 1
    elif number_of_children == 1:
        longest_path_so_far, longest_path_to_leaf = solve0(adj[node][0], adj)
        return (max(longest_path_so_far, 1 + longest_path_to_leaf),
                1 + longest_path_to_leaf)
    else:
        lps = []
        longest_path_so_far = 0
        for child in adj[node]:
            longest_path_so_far0, longest_path_to_leaf0 = solve0(child, adj)
            longest_path_so_far = max(longest_path_so_far, longest_path_so_far0)
            lps.append(longest_path_to_leaf0)

        # To longest paths to leaves.  Make a v path including this node.
        lp1, lp2 = nlargest(2, lps)
        vpath = lp1 + lp2 + 1
        longest_path_so_far = max(longest_path_so_far, lp1 + 1, vpath)
        return (longest_path_so_far, lp1 + 1)


class Solution:
    def solve(self, edges):
        indegree = defaultdict(int)
        nodes = set()
        adj = defaultdict(list)
        for u, v in edges:
            nodes.add(u)
            nodes.add(v)
            indegree[v] += 1
            adj[u].append(v)

        # Find the root and how many leaf nodes.
        for u in nodes:
            if indegree[u] == 0:
                root = u

        longest_path, _ = solve0(root, adj)
        return longest_path



def test_1():
    edges = [
        [1, 2],
        [1, 3],
        [1, 4],
        [4, 5]
    ]
    assert Solution().solve(edges) == 4

def test_2():
    """What if the tree is a straight line?"""
    edges = [
        [0, 1],
        [1, 2]
    ]
    assert Solution().solve(edges) == 3

def test_3():
    edges = [
        [0, 1],
        [1, 2],
        [1, 3]
    ]
    assert Solution().solve(edges) == 3
