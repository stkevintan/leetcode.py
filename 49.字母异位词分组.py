#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from collections import defaultdict
from typing import List

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: defaultdict[tuple, List[str]] = defaultdict(list)
        for s in strs:
            # Count characters: O(K) per string, no sorting or Counter overhead
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())
                    
# @lc code=end

