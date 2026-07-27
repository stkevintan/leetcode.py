#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deps = []
        def dfs(rt, depth):
            if rt is None: return
            nonlocal deps
            if depth >= len(deps):
                deps.append(rt.val)
            else:
                deps[depth] = rt.val
            dfs(rt.left, depth + 1)
            dfs(rt.right, depth + 1)
        dfs(root, 0)
        return deps
# @lc code=end

