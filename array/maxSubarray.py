# 53 maximum subarray https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curMax = nums[0]
        prevMax = nums[0]
        nums.pop(0)
        
        for num in nums:
            if prevMax + num < 0:
                prevMax = num
            elif num > 0 and prevMax <= 0:
                prevMax = num
            else:
                prevMax += num
            curMax = max(curMax, prevMax)
        return curMax