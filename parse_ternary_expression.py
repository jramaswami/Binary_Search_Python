"""
binarysearch.com :: Parse Ternary Expression
jramaswami
"""


class Solution:

    def solve(self, expr):

        eval_dict = {'true': True, 'false': False}

        def evaluate(e):
            print(f"evaluate({e})")
            question = e.find('?')
            if question == -1:
                # This must be just a true/false.
                return eval_dict[e.strip()]
            colon = e.rfind(':')

            answer = evaluate(e[:question].strip())
            true_condition = e[question+1:colon].strip()
            false_condition = e[colon+1:].strip()
            if answer:
                return evaluate(true_condition)
            return evaluate(false_condition)

        return evaluate(expr)


def test_1():
    s = "true ? true : false"
    expected = True
    assert Solution().solve(s) == expected


def test_2():
    s = "true ? true ? false : true : true"
    expected = False
    assert Solution().solve(s) == expected


def test_3():
    s = "true ? true ? true : true : true ? true : true"
    expected = True
    assert Solution().solve(s) == expected
