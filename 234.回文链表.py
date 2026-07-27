#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

# @lc code=start
# Definition for singly-linked list.


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get mid
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        root = slow
        # reverse p0 ~ end
        p0 = root.next
        if p0 is None:
            return True
        while p0.next:
            p1 = p0.next
            p0.next = p1.next
            p1.next = root.next
            root.next = p1

        p0 = root.next
        while p0:
            if head.val != p0.val:
                return False
            p0 = p0.next
            head = head.next
        return True
# @lc code=end

