/*
53. Maximum Subarray (https://leetcode.com/problems/maximum-subarray/)
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
*/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int previousSum = nums[0];
        int largestSum = nums[0];
        int size = nums.size();
        for (int i = 1; i < size; i++) {
            if (nums.at(i) > previousSum + nums.at(i)) {
                previousSum = nums.at(i);
            } else {
                previousSum += nums.at(i);
            }
            largestSum = max(previousSum, largestSum);

        }
        return largestSum;
    }
};
