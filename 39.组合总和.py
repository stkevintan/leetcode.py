#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        selected: List[int] = []
        def dfs(start: int, sum: int):
            if sum == target:
                yield selected.copy()
                return
            if sum > target:
                return
            for i in range(start, len(candidates)):
                selected.append(candidates[i])
                yield from dfs(i, sum + candidates[i])
                selected.pop()
        return list(dfs(0, 0))
        
# @lc code=end

