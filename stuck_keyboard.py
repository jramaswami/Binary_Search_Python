"""
binarysearch.com :: Stuck Keyboard
jramaswami
"""
class Solution:
    def solve(self, typed, target):
        typed_p = 0
        target_p = 0
        while typed_p < len(typed):
            if target_p < len(target) and typed[typed_p] == target[target_p]:
                typed_p += 1
                target_p += 1
            elif typed_p > 0 and typed[typed_p] == typed[typed_p - 1]:
                typed_p += 1
            else:
                return False
        return target_p >= len(target)



def test_1():
    typed = "aaabcccc"
    target = "abc"
    assert Solution().solve(typed, target) == True

def test_2():
    typed = "abc"
    target = "ab"
    assert Solution().solve(typed, target) == False

def test_3():
    typed = "bb"
    target = "bb"
    assert Solution().solve(typed, target) == True

def test_4():
    typed = "aaabbbbbbbcccccddddd"
    target = "abcd"
    assert Solution().solve(typed, target) == True

def test_5():
    typed = "aaabbbbbbbcccccddddd"
    target = "abbcccddddd"
    assert Solution().solve(typed, target) == True

def test_6():
    typed = "aaabbbbbbbcccccddd"
    target = "abbcccdddddd"
    assert Solution().solve(typed, target) == False
