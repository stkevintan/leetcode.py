#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        items = sorted(Counter(candidates).items())  # [(val, cnt), ...]
        res: list[list[int]] = []
        comb: list[int] = []

        def dfs(idx: int, cur: int):
            if cur == target:
                res.append(comb.copy())
                return
            if cur > target or idx == len(items):
                return
            val, cnt = items[idx]
            for k in range(cnt + 1):
                if cur + val * k > target:
                    break
                comb.extend([val] * k)
                dfs(idx + 1, cur + val * k)
                del comb[len(comb) - k:]

        dfs(0, 0)
        return res
    def combinationSum22(self, candidates: list[int], target: int) -> list[list[int]]:
        comb: list[int] = []
        candidates.sort()
        def dfs(sum: int, start: int):
            if sum == target:
                yield comb.copy()
                return
            if sum > target:
                return
            if start >= len(candidates):
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                yield from dfs(sum + candidates[i], i + 1)
                comb.pop()

        return list(dfs(0, 0))

# @lc code=end

