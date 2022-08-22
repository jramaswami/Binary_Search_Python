# Editorial for Maximum Unique Sublist

## Intuition

Dynamic programming allows us to find the longest unique sublist ending at a given index.  We can then use prefix sums to compute the sum of that sublist.

## Implementation Details

The state we keep track of in the dp array is the longest unique sublist ending at index, i.

If nums[i] has not been seen yet, then the longest unique sublist ending at index i will be one more than the longest unique sublist ending at i - 1, or dp[i-1] + 1.

If nums[i] has already been seen, then the longest unique sublist ending at index i will be the smaller of (1) one more than the longest unique sublist ending at i-1 and (2) the sublist from the previous num[i] + 1 to i.

That gives us the following formula for the transition:

```
dp[i] = d[i-1] + i if nums[i] not seen yet
        min(dp[i-1] + 1, i - prev[nums[i]]) if nums[i] seen before
```

We use prefix sums to compute the sum of the longest unique sublist ending at i for each i and keep track of the maximum as we iterate over each index.

## Time Complexity

The over all time complexity of this solution is `$\mathcal{O}(n)$`.

(1) Computing the prefix sums is `$\mathcal{O}(n)$`.

(2) Computing the longest unique sublist ending at i is done n times.  All operations except for the dictionary lookup are constant.  The dictionary lookup is constant on average, so we can call the entire computation constant. (The dictionary lookup can degrade to `$\mathcal{O}(n)$` but that occurs when there is a hash collision, which should not apply here.)

## Space Complexity

The space complexity is `$\mathcal{O}(n)$` for the dp array and the dictionary.