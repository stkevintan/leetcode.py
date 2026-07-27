#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        p1, p2 = l1, l2
        p = dummy
        while p1 or p2:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            sum = x + y + carry
            p.next = ListNode(sum % 10)
            p = p.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            carry = sum // 10
        if carry:
            p.next = ListNode(carry)
        return dummy.next
        
# @lc code=end

