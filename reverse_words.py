"""
binarysearch.com :: Reverse Words
jramaswami
"""
class Solution:
    def solve(self, sentence):
        soln = []
        # Stack will hold a word, in reverse.
        stack = []
        for c in reversed(sentence):
            # A space is found, take the word on the stack, reverse it,
            # and put it into the solution.
            if c == ' ':
                while stack:
                    soln.append(stack.pop())
                soln.append(' ')
            else:
                stack.append(c)
        # Last word on stack.
        while stack:
            soln.append(stack.pop())

        return "".join(soln)



def test_1():
    sentence = "hello there my friend"
    expected = "friend my there hello"
    assert Solution().solve(sentence) == expected
