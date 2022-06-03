"""
binarysearch.com :: Longest Even Value Path
jramaswami
"""


import collections


Result = collections.namedtuple('Result', ['curr_longest', 'actual_longest'])


class Solution:

    def solve(self, root):

        def solve0(node):
            if node is None:
                return Result(0, 0)

            left = solve0(node.left)
            right = solve0(node.right)

            if node.val % 2:
                # Odd value means no extensions of previous even paths.
                return Result(
                    0,
                    max(
                        left.actual_longest, right.actual_longest,
                        left.curr_longest, right.curr_longest
                    )
                )
            else:
                # Even value means we can extend previous paths or join them.
                return Result(
                    1 + max(left.curr_longest, right.curr_longest),
                    max(
                        left.actual_longest, right.actual_longest,
                        left.curr_longest + 1, right.curr_longest + 1,
                        1 + left.curr_longest + right.curr_longest
                    )
                )

        soln = solve0(root)
        return max(soln.curr_longest, soln.actual_longest)
