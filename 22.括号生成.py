#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets: List[str] = []
        def dfs(left: int, right: int):
            if right == n and left == n:
                yield "".join(brackets)
                return
            if right > n or left > n:
                return
            if left  - right > 0:
                brackets.append(')')
                yield from dfs(left, right + 1)
                brackets.pop()
            brackets.append('(')
            yield from dfs(left + 1, right)
            brackets.pop()
        return list(dfs(0, 0))
        
# @lc code=end

