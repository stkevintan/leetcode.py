#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        def dfs(root, curr):
            nonlocal prefix
            ans = 0
            if root is None: return 0
            curr += root.val
            ans += prefix[curr - targetSum] 
            prefix[curr] += 1
            ans += dfs(root.left, curr)
            ans += dfs(root.right, curr)
            prefix[curr] -= 1
            return ans
        return dfs(root, 0)
        
# @lc code=end

