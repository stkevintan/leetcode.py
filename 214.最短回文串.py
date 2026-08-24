#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#

# @lc code=start
class Solution:
    def shortestPalindrome_kmp(self, s: str) -> str:
        t = s + '#' + s[::-1]
        n = len(t)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and t[i] != t[j]:
                j = pi[j - 1]
            if t[i] == t[j]:
                j += 1
            pi[i] = j
        L = pi[-1]                     # 最长回文前缀长度
        return s[L:][::-1] + s
    
    def shortestPalindrome_manacher(self, s: str) -> str:
        if not s: return s
        t = f"#{'#'.join(s)}#"
        n = len(t)
        right, center = 0, 0
        max_prefix = 0
        p = [0] * n
        for i in range(n):
            if i < right:
                p[i] = min(right - i, p[2 * center - i])
            # 中心扩展
            while 0 <= i - p[i] - 1 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
            if i + p[i] > right:
                right = i + p[i]
                center = i
            if i - p[i] == 0:
                max_prefix = max(max_prefix, p[i])
        return s[max_prefix:][::-1] + s

    def shortestPalindrome(self, s: str) -> str:
        return self.shortestPalindrome_manacher(s)

# @lc code=end

