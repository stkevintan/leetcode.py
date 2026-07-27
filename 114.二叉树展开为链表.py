#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(rt):
            if rt is None: return
            dfs(rt.left)
            rm = rt.left
            if rm:
                while rm.right:
                    rm = rm.right
                rm.right = rt.right 
                rt.right = rt.left
                rt.left = None
            dfs(rt.right)
        dfs(root)
        
# @lc code=end

