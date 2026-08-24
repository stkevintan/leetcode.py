#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
from collections import defaultdict, deque
import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda p: (-p[0], p[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans

# @lc code=end

