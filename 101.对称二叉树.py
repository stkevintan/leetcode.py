#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if not left and not right: return True
            if not left or not right: return False
            return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
        return check(root.left, root.right)
# @lc code=end

