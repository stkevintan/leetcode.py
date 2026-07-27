#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = ListNode(0, head)
        p0 = head
        while p0.next:
            p1 = p0.next
            p0.next = p1.next
            p1.next = dummy.next
            dummy.next = p1
        return dummy.next
        
# @lc code=end

