# Editorial for Columns Flip To Target

First, let us take the case where we do not have to perform any column flips. Since reordering the *matrix* is free, how will we know if the *matrix* matches the *target* if the rows are out of order?  If we sort the two matrices will be equal.

Take an example:

matrix
```
0 0
1 1
1 0
```

target
```
1 1
0 0
1 0
```

When we sort them we get equal matrices:

matrix
```
0 0
1 0
1 1
```

target
```
0 0
1 0
1 1
```


Let us now take the case where we must flip some number of columns.  If we take the sorted matrices and inspect them column by column, we will find a
column where there is a mismatch.  In this case, flip the bits of the column in *matrix*, counting the operation.  Then resort the matrix and compare again.
If the column still does not match, then there is no solution; return -1.  If the comparison is equal, we can move on to the next column.

Take example 1, (which is already sorted):

matrix
```
0 0
1 0
1 1
```
target
```
0 1
1 0
1 1
```

The first column compares equal, but the second does not.  First, flip the bits in the *matrix*:

matrix
```
0 1
1 1
1 0
```

Sort the *matrix* and compare the column again:

matrix
```
0 1
1 0
1 1
```
target
```
0 1
1 0
1 1
```

Comparing the second column again now shows a match.  Return 1, which is the number of column flips we have performed.

The editorial guidelines indicate that a complexity analysis should be done, something I must admit I am not very confident doing.  However, I believe that
the worst case would be a 100x100 matrix where you must flip the bits of every column.  The initial sorting would be `$2 \times \mathcal{O}(log(n))$`. Flipping the bits would be a `$\mathcal{O}(n^2)$` operation.  Finally, sorting the matrix for each column flip would be `$\mathcal{O}(n \times n \cdot
log(n))$`.  Throwing out the smaller terms, I believe overall the solution is `$\mathcal{O}(n^2 \cdot log(n))$`.  Given, however, that the maximum n is 100, this is sufficient.

Since we work with the matrices as read, no additional space is required.

