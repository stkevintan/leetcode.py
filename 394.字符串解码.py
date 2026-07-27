#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str, cur_num = "", 0
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == '[':
                stack.append((cur_str, cur_num))
                cur_str, cur_num = "", 0
            elif c == ']':
                (prev_str, prev_num) = stack.pop()
                cur_str = prev_str + cur_str * prev_num
            else:
                cur_str += c
        return cur_str

# @lc code=end

