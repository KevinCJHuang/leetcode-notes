# 11. Container With Most Water https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        leftIndex = 0
        rightIndex = len(height) - 1
        curArea = (rightIndex - leftIndex) * min(height[leftIndex], height[rightIndex])

        while (leftIndex != rightIndex):
            if height[leftIndex] > height[rightIndex]:
                rightIndex-=1
            else:
                leftIndex += 1
            curArea = max(curArea,(rightIndex - leftIndex) * min(height[leftIndex], height[rightIndex]))
        return curArea