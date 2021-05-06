"""
binarysearch.com :: Clock Angle
jramaswami

The hour hand moves 0.5 degrees per minute
The minute hand moves 6 degrees per minute
Find the elapsed time since 0:00 to find the angle for each hand.
"""
class Solution:
    def solve(self, hour, minutes):
        elapsed = (hour * 60) + minutes
        hour_hand = (elapsed * 0.5) % 360.0
        minute_hand = (elapsed * 6.0) % 360.0
        delta = abs(hour_hand - minute_hand)
        if delta > 180.0:
            delta = 360.0 - delta
        return int(delta)


def test_1():
    assert Solution().solve(12, 22) == 121