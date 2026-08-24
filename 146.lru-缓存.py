#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
from dataclasses import dataclass


@dataclass
class LinkedListNode:
    key: int
    val: int
    prev: LinkedListNode | None = None
    next: LinkedListNode | None = None

class LinkedList:
    def __init__(self):
        self.head = LinkedListNode(0,0)
        self.end = LinkedListNode(0, 0)
        self.head.next = self.end
        self.end.prev = self.head
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def pop(self):
        if self.head.next == self.end:
            return None
        node = self.head.next
        self.remove(node)
        return node

    def append(self, node: LinkedListNode):
        prev = self.end.prev
        assert prev is not None
        prev.next = node
        node.prev = prev

        node.next = self.end
        self.end.prev = node


    


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.linked = LinkedList()

    def promote(self, node):
        self.linked.remove(node)
        self.linked.append(node)
    
    def get(self, key): 
        if key in self.map:
            node = self.map[key]
            self.promote(node)
            return node.val
        return -1
    
    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.promote(node)
            return
        if len(self.map) == self.capacity:
            node = self.linked.pop()
            if node:
                del self.map[node.key]
        node = LinkedListNode(key, value)
        self.map[key] = node
        self.linked.append(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

