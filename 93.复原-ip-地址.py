#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        cur = []
        def check_ip(ip):
            if len(ip) == 0 or len(ip) > 3:
                return False
            # 012
            if len(ip) > 1 and ip[0] == '0':
                return False
            return 0 <= int(ip) <= 255

        def dfs(start):
            if len(cur) == 3:
                last = s[start:]
                if check_ip(last):
                    yield f"{".".join(cur)}.{last}"
                return
            for i in range(1, 4):
                ip = s[start: start + i]
                if check_ip(ip):
                    cur.append(ip)
                    yield from dfs(start + i)
                    cur.pop()
        return list(dfs(0))
        
# @lc code=end

