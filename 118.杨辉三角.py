#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            row = [1] * (i + 1)
            pre = ans[-1]
            for j in range(1, i):
                row[j] = pre[j - 1] + pre[j]
            ans.append(row)
        return ans
# @lc code=end

