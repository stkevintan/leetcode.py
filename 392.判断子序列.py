#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 双指针：t 只扫一遍，s 匹配到哪算哪
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)

    def isSubsequenceDP(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        for j in range(m + 1):
            dp[0][j] = True  # 空串 s 是任意前缀的子序列
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 跳过 t[j-1]，或匹配并消耗 s[i-1]
                dp[i][j] = dp[i][j - 1] or (
                    s[i - 1] == t[j - 1] and dp[i - 1][j - 1]
                )
        return dp[n][m]

        
# @lc code=end

