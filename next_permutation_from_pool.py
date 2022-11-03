"""
binarysearch.com :: Next Permutation From Pool
jramaswami
"""
from collections import deque, Counter


class Solution:
    def solve(self, digits, lower):
        digits0 = deque(int(d) for d in digits)
        lower0 = deque(int(d) for d in lower)

        # Make them the same size
        while len(digits0) < len(lower0):
            digits0.appendleft(0)
        while len(lower0) < len(digits0):
            lower0.appendleft(0)

        digits0 = tuple(digits0)
        lower0 = tuple(lower0)

        # Get frequency of each digit in digits
        ctr = Counter(digits0)

        # While possible, make soln the same as lower.
        soln = deque()
        unwind = False
        unwind_from = 0
        for p, a in enumerate(lower0):
            if ctr[a] > 0:
                soln.append(a)
                ctr[a] -= 1
            else:
                # Find the next maximum number to place in solution.
                for i in range(a + 1, 10):
                    if ctr[i] > 0:
                        soln.append(i)
                        ctr[i] -= 1
                        break
                else:
                    # There is no d >= a in digits, so we will have to unwind
                    # from here.
                    unwind = True
                    unwind_from = p

                break

        # If we have reached the end, it is possible that lower and soln
        # are the same.  We must fix this.
        if len(soln) == len(lower0):
            unwind = True
            unwind_from = len(lower0)

        
        # Unwind until we can place a digit in soln that is greater than
        # the corresponding digit in lower0.
        if unwind:
            for a in reversed(lower0[:unwind_from]):
                # First put the current digit in soln back into frequency
                b = soln[-1]
                ctr[b] += 1
                soln.pop()

                # If there is a number available that is greater than the digit
                # in lower0, then put that here and stop.
                stop = False
                for i in range(a + 1, 10):
                    if ctr[i] > 0:
                        soln.append(i)
                        ctr[i] -= 1
                        stop = True
                        break

                if stop:
                    break

        # Fill in the soln from smallest to largest in order to minimize
        # the number.
        if len(soln) < len(lower0):
            for i in range(10):
                while ctr[i] > 0:
                    soln.append(i)
                    ctr[i] -= 1

        # Remove leading zeros.
        while soln[0] == 0:
            soln.popleft()

        return "".join(str(i) for i in soln)


def test_0():
    digits = "852"
    lower = "100"
    assert Solution().solve(digits, lower) == "258"

def test_1():
    digits = "090"
    lower = "0"
    assert Solution().solve(digits, lower) == "9"

def test_2():
    digits = "112"
    lower = "112"
    assert Solution().solve(digits, lower) == "121"

def test_3():
    digits = "113"
    lower = "112"
    assert Solution().solve(digits, lower) == "113"

def test_4():
    digits = "6802"
    lower = "917"
    assert Solution().solve(digits, lower) == "2068"
