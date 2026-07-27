#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # 只保留上一行
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            prev = 0                     # 左上角 dp[i-1][j-1]
            for j in range(1, m + 1):
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp
        return dp[m] 

        
# @lc code=end

