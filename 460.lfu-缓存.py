#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#
# @lc code=start
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Node:
    key: int = 0
    val: int = 0
    freq: int = 0
    next: Node | None  = None
    prev: Node | None = None

@dataclass
class DoubleLinkedList:
    head: Node = field(default_factory=Node)
    tail: Node = field(default_factory=Node)
    _size: int = 0

    def __post_init__(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    @property
    def size(self):
        return self._size

    def remove(self, node: Node):
        # maybe check if node is in current list?
        prev = node.prev
        next =node.next
        if prev and next:
            prev.next = next
            next.prev = prev
            self._size -= 1
    
    def append(self, node: Node):
        left = self.tail.prev or self.head
        left.next = node
        node.prev = left

        node.next = self.tail
        self.tail.prev = node
        self._size += 1

    def pop(self) -> Node | None:
        item = self.head.next
        if not item or item == self.tail:
            return None
        self._size -= 1
        sec = item.next
        assert isinstance(sec, Node)
        self.head.next = sec
        sec.prev = self.head
        return item

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.bucket: dict[int, DoubleLinkedList] = defaultdict(DoubleLinkedList)
        self.kv: dict[int, Node] = {}
        self.min_freq = 0 
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.kv:
            node = self.kv[key]
            self._inc(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            node = self.kv[key]
            node.val = value
            self._inc(node)
        elif self._ensure_capacity():
            node = Node(key, value)
            self.kv[key] = node
            self.bucket[node.freq].append(node)
            self.min_freq = node.freq

    def _inc(self, node: Node):
        self.bucket[node.freq].remove(node)
        node.freq += 1
        self.bucket[node.freq].append(node)
        # node moved from min_freq bucket
        while self.bucket[self.min_freq].size == 0:
            del self.bucket[self.min_freq]
            self.min_freq += 1

        


    def _ensure_capacity(self):
        if not self.capacity:
            return False
        if len(self.kv) < self.capacity:
            return True
        item = self.bucket[self.min_freq].pop()
        if item:
            del self.kv[item.key]
        return True



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

