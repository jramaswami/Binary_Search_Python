"""
binarysearch.com :: Next Binary Permutation
jramaswami
"""
def pandita(perm):
    """
    Pandita's algorithm for next permutation.
    REF: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    """
    # Find the largest index k such that a[k] < a[k + 1]. If no such index
    # exists, the permutation is the last permutation.
    k = -1
    for i, _ in enumerate(perm[:-1]):
        if perm[i] < perm[i+1]:
            k = max(k, i)
    
    if k < 0:
        return False

    # Find the largest index l greater than k such that a[k] < a[l].
    l = k
    for i, _ in enumerate(perm[k:], start=k):
        if perm[k] < perm[i]:
            l = max(l, i)
    
    # Swap the value of a[k] with that of a[l].
    perm[k], perm[l] = perm[l], perm[k]
    # Reverse the sequence from a[k + 1] up to and including the final element
    # a[n].
    perm[k+1:] = perm[k+1:][::-1]
    return True


def number_to_bits(n):
    """Return number as list of bits."""
    bits = []
    for b in range(33):
        mask = 1 << b
        if n & mask:
            bits.append(1)
        else:
            bits.append(0)
    return bits[::-1]


def bits_to_number(bits):
    """Return bits as a number."""
    n = 0
    m = 1
    for b in reversed(bits):
        if b:
            n += m
        m *= 2
    return n


class Solution:
    def solve(self, n):
        bits = number_to_bits(n)
        pandita(bits)
        n0 = bits_to_number(bits)
        return n0


def test_1():
    assert Solution().solve(3) == 5
