## Dynamic Programing Notes

- Thinking process
   1. (Optional) Start by solving with brute force. Then check if any calculation is repeated. Store these results in a `dpArr`.
   1. Divide the problem into sub-problems where solutions to each sub-problem is stored in `dpArr`
   1. Find a way to reuse solutions to subproblems. (i.e. how to get n from n-1, n-2, ...)
   1. Think about base cases (i.e. `len(input) == 0`, `len(input) == 1`)

- Implementation

   1. Initialize the `dpArr`
      - `dpArr` should be n-dimensional array, where `n` equals the number of inputs.
      - `len(dpArr)` is normally `len(inputArr)` or `len(inputArr)+1`.
      - `defaultValue` should be the value returned when there is "no solution".
      - Initialization syntax in Python:
        - 1d-array `dpArr = [$defaultValue] * len`
        - 2d-array `dpArr = [ [0] * len1 for i in range(len2)]`
        - This doesn't work. [It's a trap!](<https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python#:~:text=To%20initialize%20all%20values%20to,y%20in%20range(rows)%5D%20.>) `dpArr = [ [0] * len1 ] * len2`
   1. Iterate through `dpArr`. For each cell, solve the sub-problem with previous cells
   1. Return the final cell with `return dpArr[-1]`

- Complexity

   - Time Complexity: `O(n^m * l)`
      - `n` is the (max) size of one input array
      - `m` is the dimension of `dpArr`
      - `l` is the complexity for solving one sub-problem
   - Space Complexity: `O(n^m)`
      - `n` is the (max) size of one input array
      - `m` is the dimension of `dpArr`

- Tricks
   - Balance between adding one more dimension in `dpArr` vs one more `O(n)` in solving the sub-problem.
   - `len(inputArr) + 1` is super handy since we could set `dpArr[0] = base case value`. However, be aware of indexes +1 or -1 in loops
