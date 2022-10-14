# 300. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

import sys

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # DFS Brute force solution => O(2^n)
        # if (len(nums) == 0):
        #     return 0
        # maxLen = 1
        # stack = [(0, 1, nums[0])] # index, len, current max
        # stack.append((0, 0, -sys.maxsize - 1))
        # while len(stack):
        #     index, curLen, curLargest = stack.pop()
        #     if index == len(nums) - 1:
        #         continue
        #     index += 1
        #     stack.append((index, curLen, curLargest))
        #     if nums[index] > curLargest:
        #         stack.append((index, curLen + 1, nums[index]))
        #         maxLen = max(curLen + 1, maxLen)
        # return maxLen
        # 
        
        # dp solution, O(n^2)
        dp = [1] * len(nums)
        maxLen = 1
        for i in range(len(nums)):
            currentMaxLength = 1
            for j in range(0, i):
                if nums[i] > nums[j] and dp[j] + 1 > currentMaxLength:
                    currentMaxLength += 1
            dp[i] = currentMaxLength
            maxLen = max(maxLen, currentMaxLength)
        return maxLen
