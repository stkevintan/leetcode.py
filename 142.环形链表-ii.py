#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return None
        slow = head.next
        fast = head.next.next
        while fast.next and fast.next.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow != fast:
            return None
        # put slow at the begining
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        
        
# @lc code=end

