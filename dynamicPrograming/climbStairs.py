# 70. Climbing Stairs - https://leetcode.com/problems/climbing-stairs/submissions/
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        prevPrev = 1
        prev = 2
        for i in range(n-2):
            tmp = prev + prevPrev
            prevPrev = prev
            prev = tmp
        return prev