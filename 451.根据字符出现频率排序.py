#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        arr = [(-v, k) for k, v in cnt.items()]
        arr.sort()
        return "".join([k * (-v) for v, k in arr])
# @lc code=end

