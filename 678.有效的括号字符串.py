#
# @lc app=leetcode.cn id=678 lang=python3
#
# [678] 有效的括号字符串
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        minv, maxv = 0, 0
        for c in s:
            if c == '(':
                minv += 1
                maxv += 1
            elif c == ')':
                minv = max(minv - 1, 0)
                maxv -= 1
                if maxv < 0:
                    return False
            else:
                minv = max(minv - 1, 0)
                maxv += 1
        return minv <= 0
# @lc code=end

