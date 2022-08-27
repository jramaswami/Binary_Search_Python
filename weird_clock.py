"""
binarysearch.com :: Weird Clock
jramaswami
"""


class Solution:
    def solve(self, s):
        minutes_in_day = 60 * 24
        components = [int(x) for x in (s[i] for i in (0,1,3,4))]
        hh = (10*components[0]) + components[1]
        mm = (10*components[2]) + components[3]
        init_time = (60 * hh) + mm
        best_delta = minutes_in_day
        best_time = s
        for a in components:
            for b in components:
                hh = 10*a + b
                if hh < 24:
                    for c in components:
                        for d in components:
                            mm = 10*c + d
                            if 0 < mm < 60:
                                curr_time = (60 * hh) + mm
                                delta = 0
                                if (curr_time < init_time):
                                    delta = minutes_in_day - (init_time - delta)
                                if curr_time > init_time:
                                    delta = curr_time - init_time
                                if delta:
                                    if delta < best_delta:
                                        best_time = f"{hh:02}:{mm:02}"
                                        best_delta = delta
        return best_time


def test_1():
    s = "04:26"
    expected = "04:40"
    assert Solution().solve(s) == expected


def test_2():
    s = "23:59"
    expected = "22:22"
    assert Solution().solve(s) == expected


def test_3():
    "WA"
    s = "11:11"
    expected = "11:11"
    assert Solution().solve(s) == expected


def test_4():
    "WA"
    s = "00:14"
    expected = "00:40"
    assert Solution().solve(s) == expected


def test_5():
    "WA"
    s = "09:19"
    expected = "10:00"
    assert Solution().solve(s) == expected
