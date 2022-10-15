# Longest Common Subsequence https://leetcode.com/problems/longest-common-subsequence/
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Pad with row1 = 0 and col1 = 0
        dp = [[0]*(len(text2) + 1) for i in range(len(text1) + 1)]
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text2[j] == text1[i]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
                