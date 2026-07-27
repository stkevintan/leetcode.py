#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    # 中心i，边缘 j 扩展
    def expand(self, t: str, i: int, j: int = 1) -> int:
        ans = 0
        while i + j < len(t) and i - j >= 0 and t[i + j] == t[i - j]:
            ans+= 1
            j += 1
        return ans
        
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        t = "#" + "#".join(s) + '#'
        n = len(t)
        dp = [0] * n
        pivot, right = 0, 0
        for i in range(1, len(t)):
            # case 1: i >= right, do not trust any info
            if i >= right:
                dp[i] = self.expand(t, i)
            else:
                # 对称
                mirror = (pivot << 1) - i
                # case 2: dp[mirror] + i < right: 直接复用
                if dp[mirror] + i < right:
                    dp[i] = dp[mirror]
                # case 3: dp[mirror] + i >= right: 需要继续 expand 外围
                else:
                    known = right - i
                    dp[i] = known + self.expand(t, i, known + 1)
            if dp[i] + i > right:
                pivot, right = i, dp[i] + i
        index, arm = max(enumerate(dp), key=lambda x: x[1])
        start = (index - arm) // 2
        return s[start: start + arm]

    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        # 长度 1：全是回文
        for i in range(n):
            dp[i][i] = True

        # 长度 2：两字符相等
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, max_len = i, 2

        # 长度 ≥3：dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start, max_len = i, length

        return s[start:start + max_len]

        
# @lc code=end

