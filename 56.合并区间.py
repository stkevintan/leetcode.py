#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        ans = []
        cur = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= cur[1]:
                cur[1] = max(cur[1], interval[1])
            else:
                ans.append(cur)
                cur = interval
        ans.append(cur)
        return ans

# @lc code=end

