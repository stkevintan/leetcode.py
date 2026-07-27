#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: List[int] = nums[:k]
        heapq.heapify(heap)
        for d in nums[k:]:
            if d > heap[0]:
                heapq.heapreplace(heap, d)
        return heap[0]

# @lc code=end

