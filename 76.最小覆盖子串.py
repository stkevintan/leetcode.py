#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import Counter, defaultdict, deque




'''
"aab"\n"aab"\n

"aaaaaaaaaaaabbbbbcdd"
"abcdd"
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcnt = Counter(t)
        cnt = defaultdict(int)
        q = deque()
        ok = 0
        ans = ""
        def update():
             nonlocal ans, q
             if ans == "" or len(ans) > q[-1] - q[0] + 1:
                  ans = s[q[0]: q[-1] + 1]

        for (i, c) in enumerate(s):
            if c not in tcnt:
                continue
            cnt[c]+=1
            q.append(i)

            if cnt[c] == tcnt[c]:
                ok += 1
            # shrink the left boundary
            while cnt[s[q[0]]] > tcnt[s[q[0]]]:
                idx = q.popleft()
                cnt[s[idx]] -= 1
            if ok == len(tcnt):
                update()

        return ans

# @lc code=end

