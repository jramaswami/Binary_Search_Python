"""
binarysearch.com :: Polyglot Contest
jramaswami
"""


import math
import collections


class Solution:

    def solve(self, polyglots):

        # Assign and index to each language for bitmasking, *1-indexed*.
        # Make each polyglot into a bitmask.
        languages = dict()
        curr_index = 0
        polyglot_masks = []
        for polyglot in polyglots:
            polyglot_mask = 0
            for language in polyglot:
                if language not in languages:
                    languages[language] = curr_index
                    curr_index += 1
                polyglot_mask |= (1 << languages[language])
            polyglot_masks.append(polyglot_mask)

        all_covered = (1 << len(polyglots)) - 1

        # dp[language][covered]
        dp = [collections.defaultdict(lambda: math.inf) for _ in languages]
        for language_index, _ in enumerate(languages):

            language_mask = (1 << language_index)
            language_covers = 0
            for polyglot_index, polyglot_mask in enumerate(polyglot_masks):
                if language_mask & polyglot_mask:
                    language_covers |= (1 << polyglot_index)

            # Choose just this language
            dp[language_index][language_covers] = 1

            if language_index == 0:
                continue

            for covered in dp[language_index-1]:
                if dp[language_index-1][covered] < math.inf:
                    # Skip language
                    dp[language_index][covered] = min(
                        dp[language_index-1][covered],
                        dp[language_index][covered]
                    )
                    # Choose language
                    covered0 = covered | language_covers
                    dp[language_index][covered0] = min(
                        1 + dp[language_index-1][covered],
                        dp[language_index][covered0]
                    )

        soln = math.inf
        for language_index, _ in enumerate(languages):
            soln = min(soln, dp[language_index][all_covered])
        return soln


def test_1():
    languages = [["Java", "Perl"], ["C++", "Python"], ["Haskell"]]
    expected = 3
    assert Solution().solve(languages) == expected


def test_2():
    languages = [
        ["Java", "C++", "Python"],
        ["Python", "Cobol", "Java"],
        ["C++", "Haskell"],
        ["Ruby", "C++"]
    ]
    expected = 2
    assert Solution().solve(languages) == expected


def test_3():
    languages = [
        ["C", "Python", "Haskell", "Kotlin"],
        ["Java", "JavaScript", "C++", "Rust"],
        ["JavaScript", "Python", "C++"],
        ["Ruby", "C++"],
        ["Rust", "Python", "Java"]
    ]
    expected = 2
    assert Solution().solve(languages) == expected


def test_4():
    languages = [[str(i), str(-i)] for i in range(16)]
    expected = 16
    assert Solution().solve(languages) == expected