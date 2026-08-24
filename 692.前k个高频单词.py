#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
from collections import Counter
from dataclasses import dataclass
import heapq
from typing import List

@dataclass
class WordFreq:
    word: str
    freq: int 
    def __lt__(self, othr: WordFreq):
        if self.freq != othr.freq:
            return self.freq < othr.freq
        return self.word > othr.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap: list[WordFreq] = []
        for word, freq in cnt.items():
            heapq.heappush(heap, WordFreq(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = [] 
        while heap:
            ans.append(heapq.heappop(heap).word)
        return list(reversed(ans))

        
# @lc code=end

