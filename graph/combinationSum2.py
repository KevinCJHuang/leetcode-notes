# 40 Combination Sum II https://leetcode.com/problems/combination-sum-ii/
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        allPaths = []
        stack = [(0, 0, [])] # index, curSum, path
        candidates.sort()
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
                if i != index and candidates[i] == candidates[i-1]:
                    continue
                newPath = curPath.copy()
                newPath.append(candidates[i])
                stack.append((i + 1, curSum + candidates[i], newPath))
        return allPaths
