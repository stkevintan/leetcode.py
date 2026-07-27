#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# 核心：把数组当成隐式链表
#   nums[i] = 从节点 i 到节点 nums[i] 的"指针"
#   重复数 → 两个节点指向同一个节点 → 形成环
#   环入口 = 重复数
#
# 时间 O(n), 空间 O(1), 不修改原数组

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. 快慢指针找相遇点
        slow = fast = 0
        while True:
            slow = nums[slow]            # 一步
            fast = nums[nums[fast]]      # 两步
            if slow == fast:
                break

        # 2. 从头出发，与 slow 同步走，相遇点 = 环入口
        finder = 0
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return finder

        
# @lc code=end

