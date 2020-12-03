"""
binarysearch.com :: Add Binary Numbers
https://binarysearch.com/problems/Add-Binary-Numbers
"""
class Solution:
    def solve(self, aas, bbs):
        ptr = 1
        soln = []
        carry = '0'
        while len(aas) - ptr >= 0 or len(bbs) - ptr >= 0:
            if len(aas) - ptr < 0:
                a = '0'
            else:
                a = aas[len(aas) - ptr]

            if len(bbs) - ptr < 0:
                b = '0'
            else:
                b = bbs[len(bbs) - ptr]

            if a == '1' and b == '1':
                # a   b   carry
                # 1 + 1 + 0      = 0, carry 1
                # 1 + 1 + 1      = 1, carry 1
                soln.append(carry)
                carry = '1'
            elif a == '1' or b == '1':
                if carry == '1':
                    # a   b   carry
                    # 1 + 0 + 1      = 0, carry 1
                    soln.append('0')
                else:
                    # a   b   carry
                    # 1 + 0 + 0      = 0, carry 0
                    soln.append('1')
            elif a == '0' and b == '0':
                # a   b   carry
                # 0 + 0 + 1       = 1, carry 0
                # 0 + 0 + 0       = 0, carry 0
                soln.append(carry)
                carry = '0'

            ptr += 1

        if carry == '1':
            soln.append(carry)
        if not soln:
            soln = ["0"]

        return "".join(soln[::-1])

def test_1():
    a = "1"
    b = "1"
    solver = Solution()
    assert solver.solve(a, b) == "10"

def test_2():
    a = "111"
    b = "1"
    solver = Solution()
    assert solver.solve(a, b) == "1000"

def test_3():
    a = "0"
    b = "0"
    solver = Solution()
    assert solver.solve(a, b) == "0"

def test_4():
    a = "1010"
    b = "1011"
    solver = Solution()
    assert solver.solve(a, b) == "10101"
