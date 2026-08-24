#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
from collections import Counter, defaultdict, deque


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        instack = set()
        stack = deque()
        for c in s:
            if c in instack:
                cnt[c] -= 1
                continue
            while stack and stack[-1] > c and cnt[stack[-1]] > 0:
                p = stack.pop()
                instack.remove(p)
            stack.append(c)
            instack.add(c)
            cnt[c] -= 1
        return "".join(stack)
        

        
# @lc code=end

