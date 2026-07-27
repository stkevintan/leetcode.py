#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from collections import Counter
from dataclasses import dataclass
import heapq
from typing import List


@dataclass
class FreqItem:
    freq: int
    val: int
    def __lt__(self, other: FreqItem) -> bool:
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return self.topKFrequent2(nums, k) 
        return self.topKFrequent3(nums, k)

    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        nlargest = Counter(nums).most_common(k)
        return list(map(lambda x: x[0], nlargest))

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        nlargest = heapq.nlargest(k, cnt.items(), key=lambda x: x[1])
        return list(map(lambda x: x[0], nlargest))

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        freq_items: List[FreqItem] = []
        for val, freq in cnt.items():
            freq_items.append(FreqItem(freq, val))
        heap = freq_items[:k]
        heapq.heapify(heap)
        for item in freq_items[k:]:
            if item > heap[0]:
                heapq.heapreplace(heap, item)

        return list(map(lambda x: x.val, heap))

# @lc code=end

