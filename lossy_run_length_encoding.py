"""
binarysearch.com :: Lossy Run-Length Encoding
jramaswami
"""

import collections


Encoding = collections.namedtuple('Encoding', ['char', 'freq'])


def encoding_cost(freq):
    "Return the cost of encoding a letter with the given frequency."
    if freq < 1:
        return 0
    if freq == 1:
        return 1
    return len(str(freq)) + 1


class RunLengthEncoding:
    def __init__(self):
        self.total_encoding_cost = 0
        self.encoding = collections.deque()

    def encode(self, s):
        "Encode the given string."
        curr_char = s[0]
        curr_freq = 0
        for i, c in enumerate(s):
            if c != curr_char:
                self.encoding.append(Encoding(curr_char, curr_freq))
                self.total_encoding_cost += encoding_cost(curr_freq)
                curr_freq = 0
                curr_char = c
            curr_freq += 1
        self.encoding.append(Encoding(curr_char, curr_freq))
        self.total_encoding_cost += encoding_cost(curr_freq)

    def push(self, c):
        "Push the character onto the back of the current encoding."
        if self.encoding and self.encoding[-1].char == c:
            self.total_encoding_cost -= encoding_cost(self.encoding[-1].freq)
            self.encoding[-1] = Encoding(self.encoding[-1].char, self.encoding[-1].freq+1)
            self.total_encoding_cost += encoding_cost(self.encoding[-1].freq)
        else:
            self.encoding.append(Encoding(c, 1))
            self.total_encoding_cost += 1

    def pop(self):
        "Pop the first character off the current encoding."
        if self.encoding[0].freq == 1:
            self.total_encoding_cost -= encoding_cost(self.encoding[0].freq)
            self.encoding.popleft()
        else:
            self.total_encoding_cost -= encoding_cost(self.encoding[0].freq)
            self.encoding[0] = Encoding(self.encoding[0].char, self.encoding[0].freq-1)
            self.total_encoding_cost += encoding_cost(self.encoding[0].freq)

    def __str__(self):
        s = "".join(t.char * t.freq for t in self.encoding)
        return f"({self.total_encoding_cost} {s})"


class Solution:

    def solve(self, s, k):
        suffix_encoding = RunLengthEncoding()
        suffix_encoding.encode(s)
        prefix_encoding = RunLengthEncoding()
        soln = suffix_encoding.total_encoding_cost
        window = collections.deque()
        for c in s:
            window.append(c)
            suffix_encoding.pop()
            while len(window) > k:
                prefix_encoding.push(window[0])
                window.popleft()

            curr_encoding_cost = prefix_encoding.total_encoding_cost + suffix_encoding.total_encoding_cost
            if prefix_encoding.encoding and suffix_encoding.encoding:
                if prefix_encoding.encoding[-1].char == suffix_encoding.encoding[0].char:
                    curr_encoding_cost -= encoding_cost(prefix_encoding.encoding[-1].freq)
                    curr_encoding_cost -= encoding_cost(suffix_encoding.encoding[0].freq)
                    curr_encoding_cost += encoding_cost(prefix_encoding.encoding[-1].freq + suffix_encoding.encoding[0].freq)
            soln = min(soln, curr_encoding_cost)
        return soln


def test_1():
    s = "aaaaabbaaaaaccaaa"
    k = 2
    expected = 6
    assert Solution().solve(s, k) == expected
