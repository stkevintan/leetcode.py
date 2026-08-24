#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return -1
            if x + y < y + x:
                return 1
            return 0

        strs = sorted(map(str, nums), key=cmp_to_key(compare))
        result = ''.join(strs)
        return '0' if result[0] == '0' else result


# @lc code=end

