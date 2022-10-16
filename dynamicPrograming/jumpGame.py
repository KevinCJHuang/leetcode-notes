# 55. Jump Game https://leetcode.com/problems/jump-game/

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        longestJump = 0
        for i in range(len(nums)):
            longestJump = max(longestJump, nums[i] + i)
            if longestJump <= i and i != len(nums)-1:
                return False
        
        return True