"""
binarysearch.io :: Generate Primes
https://binarysearch.com/problems/Generate-Primes
"""
class Solution:
    def solve(self, n):
        if n < 2:
            return []

        prime = [True for _ in range(n+1)]
        prime[0] = prime[1] = False

        for i in range(4, n+1, 2):
            prime[i] = False

        i = 3
        while i * i <= n + 1:
            if prime[i]:
                for j in range(i+i, n+1, i):
                    prime[j] = False
            i = i + 2

        return [i for i, p in enumerate(prime) if p]

def test_1():
    solver = Solution()
    assert solver.solve(3) == [2, 3]

def test_2():
    solver = Solution()
    assert solver.solve(10) == [2, 3, 5, 7]

def test_3():
    solver = Solution()
    assert solver.solve(20) == [2, 3, 5, 7, 11, 13, 17, 19]
