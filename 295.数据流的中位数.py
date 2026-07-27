#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import heapq
from typing import List


class MedianFinder:

    def __init__(self):
        self.left: List[int] = [] # max heap
        self.right: List[int] = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.left, num)
        # 保持left.max < right.min
        heapq.heappush(self.right, heapq.heappop_max(self.left))
        # balance
        if len(self.left) < len(self.right):
            heapq.heappush_max(self.left, heapq.heappop(self.right))

    def findMedian(self) -> float:
        if 1 & (len(self.left) + len(self.right)):
            return float(self.left[0])
        return (self.left[0] + self.right[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

