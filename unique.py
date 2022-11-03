"""
binarysearch.com :: Unique String Split
"""
# len(A) + len(B) = len(B) + len(C) if AB = BC
# len(A)          =          len(C) if AB = BC

# len(A) + len(B) = len(C) + len(A) if AB = CA
#          len(B) = len(C)          if AB = CA

# len(B) + len(C) = len(A) + len(C) if BC = CA
# len(B)          = len(A)          if BC = CA

class Solution:
    def solve(self, s):

        # Compute the number of possible partitions.
        N = len(s)
        soln = (N-1)*(N-2) // 2

        # Subtract out the "bad" partitions.
        L = 1
        while 2 * L + 1 <= len(s):

            # This kind of partition could be double subtracted.
            perfect_partition = False
            if L * 3 == len(s):
                perfect_partition = True

            # AB = BC --> len(A) = len(C)
            a = L
            b = L + (len(s) - (2 * L))
            if s[:-L] == s[L:]:
                soln -= 1
                if perfect_partition:
                    L += 1
                    continue

            # AB = CA --> len(B) = len(C)
            if s[:-L] == s[-L:] + s[:-2*L]:
                soln -= 1
                if perfect_partition:
                    L += 1
                    continue

            # BC = CA --> len(B) = len(A)
            if s[L:] == s[2*L:] + s[:L]:
                soln -= 1
                if perfect_partition:
                    L += 1
                    continue

            L += 1

        return soln


def test_1():
    s = "abba"
    solver = Solution()
    assert solver.solve(s) == 3

def test_2():
    s = "aaaa"
    solver = Solution()
    assert solver.solve(s) == 0

def test_3():
    s = "ccbc"
    solver = Solution()
    assert solver.solve(s) == 3

def test_4():
    s = "ccc"
    solver = Solution()
    assert solver.solve(s) == 0


def main():
    s = "a" * 7000
    solver = Solution()
    print(solver.solve(s))

    
if __name__ == '__main__':
    main()
