# Editorial for Unique String Split

# Intuition

We are partitioning the string into three pieces, A, B, and C.  We then combine
the strings such that we have three strings for comparison, AB, BC, CA.  There
are three cases of equality:

(1) AB = BC
(2) BC = CA
(3) AB = CA

The naive solution would be to go over all possible partitions to count the
number of partitions where none of the three above equality cases occur.

### Observation 1

For any equality case to occur the comparison strings must be of equal length.
This being the case, that means that two of the substrings involved will also
be of equal length.  For example:

If AB = BC then:

(1) len(AB) = len(BC)
(2) len(A) + len(B) = len(B) + len(C)
(3) len(A) = len(C) by subtraction of len(B) from both sides of the equation.

This is true for each equality case.

### Observation 2

If you know the length of two of the substrings, call it L, you can compute the
length of the remaining substring: len(S) - (2 * L), where S is the entire
string.


### Observation 3

For any given L, we can use observation 2 to determine each possible set of
substrings and therefore each possible set of comparison strings.  We can then
determine which of the equality cases is possible for the given L.

### Observation 4

If len(S) = N, then there are (N-1) &times; (N-2) &div; partitions.

### Observation 5

Using observation 3 and 4, when we iterate over each L and subtract out any
of the equality cases to get the solution.

### Observation 6: A corner case

If L partitions S into three substrings of equal length, call it a perfect
partition, you must be careful to avoid subtracting the same partition more
than once.


## Implentation

The implementation follows the observations above.  First, compute the number
of possible partitions.  Iterate over all the possible equal lengths, L.
Determine if L is a perfect partition.  Check each equality case and subtract
it from the solution, being careful not to over subtract a perfect partition.

## Time Complexity

I believe this to be a O(N^2) time complexity.  For each equality length L,
there is the test for string equality.

## Space Complexity

No additional space is necessary, so the space complexity is O(N).

