#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next
        fast = fast.next
        while slow and fast:
            slow = slow.next
            fast = fast.next
        d = slow.next
        slow.next = d.next
        return dummy.next
        
# @lc code=end
