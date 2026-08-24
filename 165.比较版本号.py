#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_arr = version1.split('.')
        version2_arr = version2.split('.')
        n,m = len(version1_arr), len(version2_arr)
        for i in range(max(n, m)):
            a = int(version1_arr[i]) if i < n else 0
            b = int(version2_arr[i]) if i < m else 0
            if a != b:
                return -1 if a < b else 1
        return 0

        
# @lc code=end

