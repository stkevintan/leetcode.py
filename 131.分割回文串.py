#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
from typing import List


class Solution:
    def is_palindrome(self, s: str):
        return s == s[::-1]
        # i, j = 0, len(s) - 1
        # while i < j:
        #     if s[i] != s[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True
    
    def partition(self, s: str) -> List[List[str]]:
        # 用 dp 预处理
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        
        def dfs(start: int, existing: List[str]):
            if start == len(s):
                yield existing
                return
            for i in range(start, len(s)):
                # slice = s[start: i + 1]
                # if self.is_palindrome(slice):
                if dp[start][i]:
                    yield from dfs(i+1, [*existing, s[start: i + 1]])
        return list(dfs(0, []))

# @lc code=end

