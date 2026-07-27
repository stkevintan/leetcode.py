#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        s_set = set(['(', '[', '{'])
        for c in s:
            if c in s_set:
                stack.append(c)
            elif c == ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif c == ']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif c == '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
        return not stack

# @lc code=end

