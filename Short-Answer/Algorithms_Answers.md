#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity of this is simply `O(n)`. Using algebra, you can divide both the end condition and the increment by `n * n` to get what equates to a simple for loop, iterating `n` times.


b) The first for loop is of runtime complexity `O(n)` as it simply runs `n` times. The inner loop involves doubling `j` every iteration, making its growth exponential. That means that the inner loop has a runtime complexity of `O(log(n))`. Since the inner loop is run for every iteration of the outer loop, the combined runtime complexity would be `O(n*log(n))`.


c) This function will double the input number. It runs recursively and runs the function for `n - 1` each time, ending at `0`. This means the function will be run for every value from `0` to `n` exactly once, making its runtime complexity `O(n)`.

## Exercise II

To find the value of `f` in this building, we can use a binary search algorithm. To do this, we would go to the middle floor, `n / 2`, and drop an egg from there. We should go the direction that we know `f` is from our current position. If the egg did not break, we know `f` is above us, so we should go to the half-way point between our current position and the top floor, which would be `3n / 4`. If the egg did break, we know `f` is at or below our current floor, so we should go to the half-way position between our current floor and ground-level, which would be `n / 4`. We then repeat the procudure of dropping an egg and moving up if the egg did not break and moving down if the egg did break, always moving to the half-way point between our current position and the next point up or down. The "next point" is the last level we tested in that direction, unless there is none, then it would be the top floor if we're going up, or the bottom floor if we're going down. To find the half-way point between the two floors, we simply take the average of the two floors by adding them together and dividing by 2. Once we have tested two adjacent floors where the egg did not break on the lower and did break on the higher, we know that `f` is the higher of the two floors.
