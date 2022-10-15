# 139. Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if s[i-len(word)+1:i+1] == word:
                    if i-len(word)+1 == 0 or dp[i-len(word)]:
                        dp[i] = True
                        break
        return dp[-1]

