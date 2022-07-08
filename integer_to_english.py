"""
binarysearch.com :: Integer to English
jramaswami
"""


class Solution:

    def solve(self, num):
        if num == 0:
            return "Zero"

        TENS_AND_ONES_LABELS = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        TENS_LABELS = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
            "Eighty", "Ninety"
        ]

        def three_digit_string(t):
            s = []
            hundreds = int(t[0])
            if hundreds > 0:
                s.append(TENS_AND_ONES_LABELS[hundreds])
                s.append('Hundred')

            tens_and_ones = int(t[1:])
            if 1 <= tens_and_ones < 20:
                s.append(TENS_AND_ONES_LABELS[tens_and_ones])
            else:
                tens, ones = divmod(tens_and_ones, 10)
                s.append(TENS_LABELS[tens])
                if ones > 0:
                    s.append(TENS_AND_ONES_LABELS[ones])

            return " ".join(s)

        # Left-pad to 12 digits.
        num = str(num)
        num = num.rjust(12, '0')
        # Split into 3s
        buckets = (num[:3], num[3:6], num[6:9], num[9:])
        bucket_labels = ["Billion", "Million", "Thousand", ""]
        soln = []
        for i, (b, bl) in enumerate(zip(buckets, bucket_labels)):
            if b == '000':
                continue
            soln.append(three_digit_string(b))
            soln.append(bl)
        return (" ".join(soln)).strip()


def test_1():
    num = 523
    expected = "Five Hundred Twenty Three"
    assert Solution().solve(num) == expected


def test_2():
    num = 823418
    expected = "Eight Hundred Twenty Three Thousand Four Hundred Eighteen"
    assert Solution().solve(num) == expected


def test_3():
    num = 700
    expected = "Seven Hundred"
    assert Solution().solve(num) == expected


def test_4():
    num = 0
    expected = "Zero"
    assert Solution().solve(num) == expected


def test_5():
    num = 234896000000
    expected = "Two Hundred Thirty Four Billion Eight Hundred Ninety Six Million"
    assert Solution().solve(num) == expected


def test_6():
    num = 692400455
    expected = "Six Hundred Ninety Two Million Four Hundred Thousand Four Hundred Fifty Five"
    assert Solution().solve(num) == expected
