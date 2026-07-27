#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from math import inf
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBST2(root, rmin, rmax):
            if root is None:
                return True
            if root.val <= rmin or root.val >= rmax:
                return False
            return isValidBST2(root.left, rmin, root.val) and isValidBST2(root.right, root.val, rmax)
        return isValidBST2(root, -inf, inf)
# @lc code=end

