#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last: dict[str, int] = {c: i for i ,c in enumerate(s)}
        ans: List[int] = []
        cur_right = 0
        for i, c in enumerate(s):
            if i > cur_right:
                ans.append(i)
            cur_right = max(cur_right, last[c])
        ans.append(len(s))
        return [(b - a) for a ,b in zip([0, *ans], ans)]
# @lc code=end

