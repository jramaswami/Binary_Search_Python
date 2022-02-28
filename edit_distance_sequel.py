"""
binarysearch.com :: Edit Distance Sequel
jramaswami
"""


import collections
import functools


class Solution:

    def solve(self, source, target):
        def count_ops(T):
            dlt = ins = 0
            for op in T:
                if op[0] == '+':
                    ins += 1
                elif op[0] == '-':
                    dlt += 1
            return ins, dlt

        @functools.cache
        def solve0(s, t):
            if s >= len(source) and t >= len(target):
                return ()

            if s >= len(source):
                x = collections.deque(solve0(s, t+1))
                x.appendleft(f"+{target[t]}")
                return tuple(x)

            if t >= len(target):
                x = collections.deque(solve0(s+1, t))
                x.appendleft(f"-{source[s]}")
                return tuple(x)

            if source[s] == target[t]:
                x = collections.deque(solve0(s+1, t+1))
                x.appendleft(f"{source[s]}")
                return tuple(x)

            # Delete here.  This moves the source index forward.
            x = collections.deque(solve0(s+1, t))
            insx, dltx = count_ops(x)
            # Insert here
            y = collections.deque(solve0(s, t+1))
            insy, dlty = count_ops(y)
            dltx += 1
            totx = dltx + insx
            insy += 1
            toty = insy + dlty
            if totx < toty:
                x.appendleft(f"-{source[s]}")
                return tuple(x)
            elif totx > toty:
                y.appendleft(f"+{target[t]}")
                return tuple(y)
            else:
                if dltx >= dlty:
                    x.appendleft(f"-{source[s]}")
                    return tuple(x)
                else:
                    y.appendleft(f"+{target[t]}")
                    return tuple(y)

        return list(solve0(0, 0))


def test_1():
    source = "aab"
    target = "abb"
    expected = ["a", "-a", "b", "+b"]
    result = Solution().solve(source, target)
    assert result == expected


def test_2():
    source = "aaab"
    target = "aabb"
    expected = ["a", "a", "-a", "b", "+b"]
    result = Solution().solve(source, target)
    assert result == expected


def test_3():
    source = "abc"
    target = "cba"
    expected = ["-a", "-b", "c", "+b", "+a"]
    result = Solution().solve(source, target)
    assert result == expected


def test_4():
    source = "bcd"
    target = "acd"
    expected = ["-b", "+a", "c", "d"]
    result = Solution().solve(source, target)
    assert result == expected


def test_5():
    source = 'gqhdausadyfsozuerncognjgsbazlfbnwyutaxhwbusxpfgpsjpfgqayemzzwbchaamqfyxllsbgbkuevqgkliimruqhkldjonenmtfnwxvjfuofobfwjgmbcsukpfzputjektrafkqfkidnwtwahwqgkznmqftowhpxlcafsnzycphhgknieqrjrnueqmeagmtneecrzljonmuymvsbcacwhqdcxzooyksrthmctjcolkjeivhngctxclbfxldiqjsagamsgmygehhrawonryyrkppptmgamwmxbgeywrlzxktshllneifspcqseditfflozhprlnlhdgtmtzclgxsaxlhayrrzfgrgkzfstaftoewrrtgbsrwmjnlboobgudebvtufjltchewhshlwpnksdkgjnolavujhstmrtgddopixwezsxypebxpqwviricvfngazhealbjjfbfucfrxyktlznyzsgtqslewxcjiakuboxllx'
    target = 'ehcotggthvxzcwyjgqsisocwwwlamqjfnyfjxzmctgkdswftzytnzhnlnqoyjlrqwiganwwbgdufrbwjkyhydcgqwpwfspglxvsfrphoyznlfuacqvastsjqvwpprjxmgaqphamtkgbuwjbyvvadwuworfhzecydzzlljwmxubrftbfiybsidoxexzqfidxufpgbhtfvggsskwndbiaslrwhehlabscdghjuqhapcecndkfqtjnwuitgydopmarwcxaytrazqhraqstnwoxfjitddgsbkvlbutgxqlamirsfohopjazqktlhzhozboacvtknnnguscydtihechmrelmxwamoroihfxdoogktggmjybmzwahzwvyuzuhwuvethlfspphuhimoousrbjcetarhwmxgnbowdwpncoxehwsrbxjrzcxxxpammtttuohmtgryzqdqefcjyunobivcjpthvqiplzomdwdhafzwqxaamsfovugm'
    expected = ["-b", "+a", "c", "d"]
    result = Solution().solve(source, target)
    assert result == expected
