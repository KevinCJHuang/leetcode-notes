# Combination Sum https://leetcode.com/problems/combination-sum/
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
#     Backtracking / recursion
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         rv = []
#         candidates.sort()

#         def backtracking(start, curSum, path):
#             if curSum > target:
#                 return
#             if curSum == target:
#                 rv.append(path.copy())
#                 return

#             for i in range(start, len(candidates)):
#                 path.append(candidates[i])
#                 backtracking(i, curSum + candidates[i], path)
#                 path.pop()

#         backtracking(0, 0, [])
#         return rv

# Iteration
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        allPaths = []
        stack = [(0, 0, [])] # index, curSum, path
        while stack:
            tup = stack.pop()
            index = tup[0]
            curSum = tup[1]
            curPath = tup[2]
            if curSum > target:
                continue
            if curSum == target:
                allPaths.append(curPath)
            for i in range(index, len(candidates)):
                newPath = curPath.copy()
                newPath.append(candidates[i])
                stack.append((i, curSum + candidates[i], newPath))
        return allPaths