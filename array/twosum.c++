/*
1 - Two Sum (https://leetcode.com/problems/two-sum/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include "../utils/printVec.c++"
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            const int diff = target - nums[i];
            if (map.count(diff)) {
                return {map[diff], i};
            } else {
                map[nums[i]] = i;
            }
        }
        return {};
    }
};

int main () {
  Solution solution;
  vector<int> input{1,2,3,4,5};
  const vector<int> result = solution.twoSum(input, 7);
  printVec<int>(result);
}
