#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 排序让重复元素相邻
        n = len(nums)
        cur = []

        def dfs(start):
            yield cur.copy()  # 每个节点都是一个子集
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # 同一层跳过重复值
                cur.append(nums[i])
                yield from dfs(i + 1)
                cur.pop()

        return list(dfs(0))
        
# @lc code=end

