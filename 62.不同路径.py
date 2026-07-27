#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    # or  C(n, k) = C(n-1, k-1) + C(n-1, k)
    def c(self, r: int, n: int) -> int:
        r = min(r, n - r)
        ans = 1
        for c in range(1, r + 1):
            ans = ans * (n + c - r) // c
        return ans
        
    def uniquePaths(self, m: int, n: int) -> int:
        return self.c(m - 1, m + n - 2)
        
# @lc code=end

