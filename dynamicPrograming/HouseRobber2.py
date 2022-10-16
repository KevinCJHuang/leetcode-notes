# 213. House Robber II https://leetcode.com/problems/house-robber-ii/

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def robHelper(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dpArr = [0] * (len(nums))
        dpArr[0] = nums[0]
        dpArr[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dpArr[i] = max(dpArr[i-2] + nums[i], dpArr[i-1])
        return dpArr[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))
