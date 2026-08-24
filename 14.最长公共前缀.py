#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        for i in range(min([len(s) for s in strs])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if c != strs[j][i]:
                    return "".join(ans)
            ans.append(c)
        
        return "".join(ans)
                    
        
# @lc code=end

