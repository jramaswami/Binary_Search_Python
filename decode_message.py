"""
binarysearch.com :: Decode Message
https://binarysearch.com/problems/Decode-Message
"""

class Solution:
    def solve(self, message):
        dp = [0 for _ in range(len(message)+1)]
        dp[0] = 1

        for i, digit in enumerate(message):
            if digit == '1':
                # This can be interpreted as a one or two character code
                dp[i+1] += dp[i]
                if i+2 < len(dp):
                    dp[i+2] += dp[i]
            elif digit == '2':
                if i + 1 < len(message) and int(message[i+1]) <= 6:
                    # This can be interpreted as a one or two character code
                    dp[i+1] += dp[i]
                    if i+2 < len(dp):
                        dp[i+2] += dp[i]
                else:
                    # This can be interpreted as a one code
                    dp[i+1] += dp[i]
            elif digit == '0':
                # This must have been part of a two parter already taken
                # care of, so don't do anything here.
                pass
            else:
                dp[i+1] += dp[i]

        print(dp)
        return dp[-1]

def test_1():
    solver = Solution()
    message = "111"
    assert solver.solve(message) == 3

def test_2():
    solver = Solution()
    message = "8"
    assert solver.solve(message) == 1

def test_3():
    solver = Solution()
    message = "12"
    assert solver.solve(message) == 2

def test_4():
    solver = Solution()
    message = "30"
    assert solver.solve(message) == 0
