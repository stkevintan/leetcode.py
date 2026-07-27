#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import Iterator, List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start: int, subset: List[int]) -> Iterator[List[int]]:
            yield subset
            for i in range(start, len(nums)):
                yield from dfs(i + 1, [*subset, nums[i]])

        return list(dfs(0, []))
# @lc code=end

