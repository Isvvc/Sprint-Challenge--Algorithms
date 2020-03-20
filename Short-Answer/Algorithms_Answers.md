#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity of this is simply `O(n)`. Using algebra, you can divide both the end condition and the increment by `n * n` to get what equates to a simple for loop, iterating `n` times.


b) The first for loop is of runtime complexity `O(n)` as it simply runs `n` times. The inner loop involves doubling `j` every iteration, making its growth exponential. That means that the inner loop has a runtime complexity of `O(log(n))`. Since the inner loop is run for every iteration of the outer loop, the combined runtime complexity would be `O(n*log(n))`.


c) This function will double the input number. It runs recursively and runs the function for `n - 1` each time, ending at `0`. This means the function will be run for every value from `0` to `n` exactly once, making its runtime complexity `O(n)`.

## Exercise II

Setting `f` as large as possible would minimize the number of broken eggs and thus the number of dropped + broken eggs. If `f` can only be as large as `n`, then `f = n` would result in only eggs dropped from the top floor to be broken. If it can be larger than `n`, then `f = n + 1` would result in no eggs breaking. Each solution has a runtime complexity of `O(1)`.
