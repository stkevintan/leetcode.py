#
# @lc app=leetcode.cn id=554 lang=python3
#
# [554] 砖墙
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        bricks = defaultdict(int)
        for line in wall:
            sum = 0
            for brick in line[:-1]:
                sum += brick
                bricks[sum] += 1
    
        ans = 0
        for c in bricks.values():
            ans = max(ans, c)
        return len(wall) - ans
        
# @lc code=end

