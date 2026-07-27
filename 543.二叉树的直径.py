#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(rt):
            nonlocal ans
            if rt is None:
                return 0
            left = dfs(rt.left)
            right = dfs(rt.right)
            ans = max(ans, left + right)

            return 1 + max(left, right)

        dfs(root)

        return ans

        
# @lc code=end

