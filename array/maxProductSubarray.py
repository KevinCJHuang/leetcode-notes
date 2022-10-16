# 152. Maximum Product Subarray https://leetcode.com/problems/maximum-product-subarray/

# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # This question is kind of like a dp question, where we store previous results
        # and get the current result from previous results

        if len(nums) == 0:
            return 0

        curMax = nums[0]
        curMin = nums[0]
        rv = nums[0]
        
        for i in range(1, len(nums)):
            tempMax = curMax * nums[i]
            tempMin = curMin * nums[i]
            curMax = max(nums[i], tempMax, tempMin)
            curMin = min(nums[i], tempMax, tempMin)
            rv = max(curMax, rv)
        return rv