/*
217. Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
*/

#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set;
        const int size = nums.size();
        for (int i = 0; i < size; i++) {
            if (set.find(nums[i]) != set.end()) {
                return true;
            }
            set.insert(nums[i]);
        }
        return false;
    }
};

/*
Notes:
- unordered_set uses a hashmap; ordered_set uses a b-tree. Use unordered_set whenever possible.
- Same for unordered_map vs. ordered_map
- Most collection data structures in c++ use container.find(element) != container.end() to check if it contains an element.


One-liner solution from leetcode discussion:
https://leetcode.com/problems/contains-duplicate/discuss/60898/Single-line-C%2B%2B-solution-60ms

class Solution {
  public:
    bool containsDuplicate(vector<int>& nums) {
        return nums.size() > unordered_set<int>(nums.begin(), nums.end()).size();
    }
};
*/