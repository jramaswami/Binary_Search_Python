"""
binarysearch.com :: Ancient Astronaut Theory
jramaswami
"""


class Solution:
    def solve(self, dictionary, s):
        location = {c: i for i, c in enumerate(dictionary)}
        print(location)
        curr_min = math.inf
        for c in reversed(s):
            # Is there any letter with a lower index than me to my right?
            if c in location:
                t = location[c]
                if t > curr_min:
                    return False
                curr_min = min(curr_min, t)
        return True