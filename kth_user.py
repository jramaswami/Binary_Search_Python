"""
binarysearch.com :: Weekly Contest 42 :: Kth User to Visit Website
https://binarysearch.com/room/Weekly-Contest-42-B2uSxptT2C?questionsetIndex=2
jramaswami
"""
class Solution:
    def solve(self, requests, k):
        events = []
        for i, (b, e) in enumerate(requests):
            events.append((b, 1, i))
            events.append((e+1, 0, i))

        events.sort()
        can_be_kth = set()
        previous_visitors = 0
        current_visitors = 0
        new_visitors = set()
        for timer, etype, visitor in events:
            if etype == 0:
                new_visitors.discard(visitor)
                current_visitors -= 1
                previous_visitors += 1
            else:
                new_visitors.add(visitor)
                current_visitors += 1

            min_visitor = previous_visitors
            max_visitor = current_visitors + previous_visitors - 1
            if k >= min_visitor and k <= max_visitor:
                can_be_kth.update(new_visitors)
                new_visitors = set()

            if previous_visitors > k:
                break

        return list(sorted(can_be_kth))


def test_1():
    requests = [
        [3, 4],
        [1, 3],
        [4, 4]
    ]
    k = 1
    assert Solution().solve(requests, k) == [0, 1, 2]

def test_2():
    requests = [
        [0, 0],
        [0, 0],
        [1, 1],
        [2, 2],
        [2, 2]
    ]
    k = 3
    assert Solution().solve(requests, k) == [3, 4]

def test_3():
    requests = [
        [60, 70],
        [0, 10],
        [11, 30],
        [22, 40]
    ]
    k = 1
    assert Solution().solve(requests, k) == [2, 3]
