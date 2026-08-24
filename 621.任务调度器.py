#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
from collections import defaultdict, Counter
import heapq
from typing import List


class Solution:
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        heap = []
        freq = defaultdict(int)
        for task in tasks:
            heapq.heappush(heap, (freq[task] * (1 + n), task))
            freq[task] += 1
        
        t = 0
        while heap:
            (min_t, task) = heapq.heappop(heap)
            if t < min_t:
                t = min_t
            t += 1
        return t

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        cnt = list(freq.values()).count(max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + cnt)
        
# @lc code=end

