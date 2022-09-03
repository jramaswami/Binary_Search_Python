"""
binarysearch.com :: Seat Arrangement
jramaswami
"""


class Solution:
    def solve(self, n, seats):
        # Boundary cases.
        if n == 0:
            return True

        if len(seats) == 1:
            if seats == [0]:
                return n <= 1
            return False

        # Greedy
        seatslr = list(seats)
        m = 0
        for i, _ in enumerate(seatslr):
            if i == 0:
                if seatslr[i] == 0 and seatslr[i+1] == 0:
                    seatslr[i] = 1
                    m += 1
            elif i + 1 >= len(seatslr):
                if seatslr[i-1] == 0 and seatslr[i] == 0:
                    seatslr[i] = 1
                    m += 1
            else:
                if seatslr[i-1] == 0 and seatslr[i] == 0 and seatslr[i+1] == 0:
                    seatslr[i] = 1
                    m += 1
        if m == n:
            return True

        m = 0
        seatsrl = list(seats)
        for i in range(len(seatsrl) - 1, -1, -1):
            if i == 0:
                if seatsrl[i] == 0 and seatsrl[i+1] == 0:
                    seatsrl[i] = 1
                    m += 1
            elif i + 1 >= len(seatsrl):
                if seatsrl[i-1] == 0 and seatsrl[i] == 0:
                    seatsrl[i] = 1
                    m += 1
            else:
                if seatsrl[i-1] == 0 and seatsrl[i] == 0 and seatsrl[i+1] == 0:
                    seatsrl[i] = 1
                    m += 1
        return m == n


def test_1():
    n = 2
    seats = [0, 0, 1, 0, 0, 0, 1]
    expected = True
    assert Solution().solve(n, seats) == expected


def test_2():
    n = 1
    seats = [0, 1, 0]
    expected = False
    assert Solution().solve(n, seats) == expected


def test_3():
    "RTE"
    n = 0
    seats = [0]
    expected = True
    assert Solution().solve(n, seats) == expected


def test_4():
    "WA"
    n = 1
    seats = [0, 0, 0]
    expected = True
    assert Solution().solve(n, seats) == expected