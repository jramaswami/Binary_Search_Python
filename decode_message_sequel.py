"""
binarysearch.com :: Decode Messages Sequel
jramaswami
"""


def solve0(index, message, acc):
    """Recursive solution."""
    print('\t' * (index + 1), 'solve0', index, message, acc)
    if index >= len(message):
        return acc

    # This index as a separate number.
    if message[index] == '*':
        result = solve0(index + 1, message, acc * 9)
    else:
        result = solve0(index + 1, message, acc)

    # Can we do this index + 1 as a number?
    if index + 1 < len(message):
        # *x
        if message[index] == '*':
            # *x = 1x
            result += solve0(index + 2, message, acc * 1)
            # *x = 2x
            if int(message[index + 1]) <= 6:
                result += solve0(index + 1, message, acc * 1)
        # 1*
        elif message[index] == '1' and message[index + 1] == '*':
            result += solve0(index + 2, message, acc * 9)
         # 2*
        elif message[index] == '2' and message[index + 1] == '*':
            result += solve0(index + 2, message, acc * 6)
        # 1x
        elif message[index] == '1':
            result += solve0(index + 2, message, acc * 1)
        # 2x
        elif message[index] == '2' and int(message[index + 1]) <= 6:
            result += solve0(index + 2, message, acc * 1)

    return result


class Solution:
    def solve(self, message):
        return solve0(0, message, 1)


def test_1():
    message = "1*"
    assert Solution().solve(message) == 18

def test_2():
    message = "22"
    assert Solution().solve(message) == 2

def test_3():
    message = "*00"
    assert Solution().solve(message) == 0