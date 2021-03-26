"""
binarysearch.com :: Reverse Words
jramaswami
"""
class Solution:
    def solve(self, sentence):
        return " ".join(reversed(sentence.split()))
