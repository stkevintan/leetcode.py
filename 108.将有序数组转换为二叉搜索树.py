#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 0:
            return None
        m = (len(nums) - 1) >> 1
        return TreeNode(nums[m], self.sortedArrayToBST(nums[0:m]), self.sortedArrayToBST(nums[m + 1:]))
        
# @lc code=end

