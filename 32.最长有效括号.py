#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        for i, c in enumerate(s):
            if i == 0 or c == '(': continue
            # if (...)
            if i - 1 - dp[i - 1] >=0 and s[i - 1 - dp[i - 1]] == '(':
                dp[i] = dp[i - 1] + 2
                # merge prev dp
                if i - 2 - dp[i - 1] >= 0:
                    dp[i] += dp[i - 2 - dp[i - 1]]
        return max(dp) if dp else 0


    def longestValidParentheses1(self, s: str) -> int:
        stack = [-1]          # 栈底放 -1 当"最后一个无效位置的索引"
        ans = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)       # 当前 ')' 是多余的，记为新起点
                else:
                    ans = max(ans, i - stack[-1])
        return ans
        

# @lc code=end

