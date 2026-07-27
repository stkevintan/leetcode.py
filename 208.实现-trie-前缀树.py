#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start

from dataclasses import dataclass, field

@dataclass
class TireNode:
    children: dict[str, TireNode] = field(default_factory=dict)
    is_end: bool = False

class Trie:

    def __init__(self):
        self.root = TireNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TireNode()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root 
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

