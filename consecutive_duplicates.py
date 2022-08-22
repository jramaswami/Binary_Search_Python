"""
binarysearch.com :: Consecutive Duplicates
jramaswami

Use a stack to hold the string with no duplicates.
For each letter is s, if S is empty or the top of S is not the current letter
push the letter onto the stack.  If the top of the stack is the same as the
current letter, then discard that letter.

This is done in O(N) time because we only consider each letter of S once.  When
considering S, the stack operations are all O(1).  The join at the end is also
O(N).

We require O(N) extra space for our stack.
"""


class Solution:
    def solve(self, S):
        stack = []
        for c in S:
            if not stack or stack[-1] != c:
                stack.append(c)
        return "".join(stack)


def test_1():
    S = "YYYXYXX"
    expected = "YXYX"
    assert Solution().solve(S) == expected