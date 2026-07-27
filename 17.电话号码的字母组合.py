#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List



class Solution:
    def __init__(self):
        self._buttons = dict[str, list[str]]()
        step = [0, 0, 3, 3, 3, 3, 3, 4, 3, 4]
        offset = 0
        for i in range(2, 10):
            c = chr(ord('0') + i)
            self._buttons[c] = []
            for _ in range(step[i]):
                self._buttons[c].append(chr(ord('a') + offset))
                offset += 1
    
    def letterCombinations(self, digits: str) -> List[str]:
        comb: List[str] = []
        def dfs(start: int):
            if start == len(digits):
                yield "".join(comb)
                return

            for u in self._buttons[digits[start]]:
                comb.append(u)
                yield from dfs(start + 1)
                comb.pop()

        return list(dfs(0))
                

    def letterCombinations1(self, digits: str) -> List[str]:
        ans = []
        for d in digits:
            if len(ans) == 0:
                ans = self._buttons[d]
                continue
            tmp = []
            for c in self._buttons[d]:
                for prefix in ans:
                    tmp.append(prefix + c)
            ans = tmp
        return ans

# @lc code=end

