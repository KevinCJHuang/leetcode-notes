## Dynamic Programing Notes

- DP can be used when a problem can be divided into similar sub-problems, and their results can be reused. The solution of the sub-problems are combined to get the final solution
- Steps:
  - Divide the problem into a sub-problem (i.e. how to get n from n-1, n-2, ...)
  - Solve the sub-problem
  - Iterate through the input and solve all sub-problems
  - return the solution to the last sub-problem
- initialize dp array: `dp = [$defaultValue] * len(inputs)`
