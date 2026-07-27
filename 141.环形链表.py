#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None or head.next.next is None:
            return False
        slow, fast = head.next, head.next.next
        while fast.next and fast.next.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        return slow == fast
        
# @lc code=end

