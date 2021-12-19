"""
binarysearch.com :: String Expansion
jramaswami
"""


import collections
import enum


class TType(enum.Enum):
    string = enum.auto()
    number = enum.auto()
    open_p = enum.auto()
    close_p = enum.auto()


Token = collections.namedtuple('Token', ['value', 'type'])


class Solution:
    def solve(self, s):

        def tokenize(s):
            tokens = []
            number = 0
            parsing_number = False
            string = []
            parsing_string = False
            for c in s:
                if c.isdigit():
                    parsing_number = True
                    number *= 10
                    number += int(c)
                else:
                    if parsing_number:
                        tokens.append(Token(number, TType.number))
                        number = 0
                        parsing_number = False

                if c.isalpha():
                    parsing_string = True
                    string.append(c)
                else:
                    if parsing_string:
                        tokens.append(Token("".join(string), TType.string))
                        string = []
                        parsing_string = False

                if c == '(':
                    tokens.append(Token(c, TType.open_p))

                if c == ')':
                    tokens.append(Token(c, TType.close_p))

            if parsing_string:
                tokens.append(Token("".join(string), TType.string))
                string = []
                parsing_string = False

            return tokens

        def decode(tokens, start_index):
            # print(f"decode(... {start_index=})")
            result = []
            i = start_index
            multiplier = 1
            while i < len(tokens):
                token = tokens[i]
                if token.type == TType.string:
                    result.append(multiplier * token.value)
                    i += 1
                    multiplier = 1
                elif token.type == TType.number:
                    multiplier = token.value
                    i += 1
                elif token.type == TType.open_p:
                    i, T = decode(tokens, i + 1)
                    result.append(multiplier * T)
                    multiplier = 1
                elif token.type == TType.close_p:
                    i += 1
                    break
            return i, "".join(result)

        tokens = tokenize(s)
        _, soln = decode(tokens, 0)
        return soln


def test_1():
    s = "3(a)2(bc)"
    expected = "aaabcbc"
    assert Solution().solve(s) == expected


def test_2():
    s = "3(a2(c))"
    expected = "accaccacc"
    assert Solution().solve(s) == expected


def test_3():
    s = "2(abc)3(cd)ef"
    expected = "abcabccdcdcdef"
    assert Solution().solve(s) == expected


def test_4():
    s = "abc3(cd)xyz"
    expected = "abccdcdcdxyz"
    assert Solution().solve(s) == expected



def test_5():
    s = "2(ye)0(z)2(2(po)w)"
    expected = "yeyepopowpopow"
    assert Solution().solve(s) == expected
