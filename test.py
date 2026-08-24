# ABCD => key1 1<<26
# 0 ~ 9 => key2  1<<10

# CTRL, ALT, SHIFT, key3

# modifier => "! @ CTRL ALT" => key ()

# (key1, key2, key3)

# O(1)
# dict[]

from collections import defaultdict
from dataclasses import dataclass
from typing import List, Tuple

modifier = ['CTRL', 'SHIFT', 'ALT', 'WIN']

bucket = ['~', '!', '#', '$', '%', '^', '&', '@']

def is_modifier(s: str):
    return s in modifier

def modifier_index(s: str):
    for i, m in enumerate(modifier):
        if m == s:
            return i
    return -1

def hash_special(special: dict[str, int])-> str:
    ans: List[str] = []
    for ch in bucket:
        cnt = special[ch]
        if cnt > 0:
            ans.append(ch + str(cnt))
    return "".join(ans)

def parse(keystrokes: List[str]):
        speical: dict[str, int] = defaultdict(int)
        alpha, digit, modifier = 0, 0, 0
        for key in keystrokes:
            key = key.upper()
            if key.isdigit():
                digit |= 1 << (ord(key) - ord('0'))
                continue
            if len(key) == 1 and key.isalpha():
                alpha |= 1 << (ord(key)- ord('A'))
                continue
            idx = modifier_index(key)
            if idx != -1:
                modifier |= 1 << idx
                continue
            speical[key] += 1
        special_key = hash_special(speical)
        return (alpha, digit, modifier, special_key)

class Solution:
    def __init__(self):
        self.dict: dict[Tuple[int, int, int, str], str] = {}

    def encode(self, keystrokes: List[str]) -> Tuple[int, int, int, str]:
        return parse(keystrokes)

    def get(self, param: str):
        keybinding = self.encode(param.split(' '))
        return self.dict.get(keybinding, None)
        
    def set(self, param: str):
        keywords = param.split(' ')
        keybinding = self.encode(keywords[:-1])
        command = keywords[-1]
        self.dict[keybinding] = command


solution = Solution()

print("#1", solution.get('CTRL C'))
solution.set('CTRL C COPY')
print("#2", solution.get('CTRL C'))
print("#3", solution.get('C CTRL'))
print("#4", solution.get('ctrl C'))

solution.set('CTRL C PASTE')
print("#5", solution.get('CTRL C'))

solution.set('CTRL SHIFT T REFRESH')
print("#6", solution.get('CTRL SHIFT T'))
solution.set('CTRL SHIFT $ # @ REFRESH')
print("#7", solution.get('CTRL SHIFT # $ @'))
print("#8", solution.get('CTRL SHIFT # $'))
