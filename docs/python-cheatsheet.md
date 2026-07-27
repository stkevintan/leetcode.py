# Python 常用语法 & 内置库 CheatSheet

---

## 一、基础语法

### 1.1 变量 & 类型

```python
a: int = 1
b: float = 3.14
c: str = "hello"
d: bool = True
e: None = None

# 多变量赋值
x = y = z = 0
a, b = 1, 2

# 类型转换
int("42")       # 42
str(42)         # "42"
float("3.14")   # 3.14
bool(0)         # False
```

### 1.2 条件 & 循环

```python
# if-elif-else
if x > 0:
    pass
elif x == 0:
    pass
else:
    pass

# 三元表达式
a = x if x > 0 else -x

# for 循环
for i in range(5):        # 0,1,2,3,4
for i in range(2, 5):     # 2,3,4
for i in range(0, 10, 2): # 0,2,4,6,8

# 反向遍历
for i in range(n - 1, -1, -1):

# while
while condition:
    break    # 跳出循环
    continue # 跳过本次迭代
```

### 1.3 函数

```python
def func(a: int, b: int = 0) -> int:
    """文档字符串"""
    return a + b

# lambda
add = lambda x, y: x + y
sorted(nums, key=lambda x: -x)

# *args, **kwargs
def f(*args, **kwargs):
    print(args)    # tuple
    print(kwargs)  # dict
```

---

## 二、数据结构

### 2.1 list

```python
lst = [1, 2, 3]
lst.append(4)          # 末尾追加
lst.pop()              # 弹出末尾
lst.pop(0)             # 弹出索引0
lst.insert(1, 99)      # 在索引1插入
lst.remove(3)          # 删除第一个值=3
lst.index(3)           # 查找索引

# 切片
lst[start:end:step]    # 不包含 end
lst[::-1]              # 反转
lst[-1]                # 最后一个

# 排序
lst.sort()             # 原地排序
lst.sort(reverse=True)
sorted(lst)            # 返回新列表
sorted(lst, key=lambda x: (x[0], -x[1]))  # 多级排序
```

### 2.2 list 作为栈 / 队列

```python
# 栈 (LIFO)
stack = []
stack.append(1)
stack.pop()            # 弹出 1

# 队列 (FIFO) — 用 deque
from collections import deque
q = deque()
q.append(1)
q.popleft()            # 弹出 1（O(1)）
```

### 2.3 dict

```python
d = {'a': 1, 'b': 2}
d['c'] = 3
d.get('x', 0)          # 不存在返回默认值 0
d.setdefault('x', 0)   # 不存在则设置
d.pop('a')             # 删除并返回
del d['b']             # 直接删除

# 遍历
for k, v in d.items():
for k in d:
for v in d.values():

# 合并字典
d1 | d2                # Python 3.9+
{**d1, **d2}           # 旧写法
```

### 2.4 set

```python
s = {1, 2, 3}
s.add(4)
s.remove(2)            # 不存在会报错
s.discard(99)          # 不存在不报错

# 集合运算
a & b    # 交集
a | b    # 并集
a - b    # 差集
a ^ b    # 对称差
```

### 2.5 tuple

```python
t = (1, 2, 3)
a, b, c = t            # 解包
```

---

## 三、推导式 (Comprehensions)

```python
# list
[i for i in range(10) if i % 2 == 0]
[i if i > 0 else 0 for i in nums]

# 二维
[[0] * n for _ in range(m)]    # ✅ 正确
# [[0] * n] * m                # ❌ 每行共享引用

# dict
{k: v for k, v in d.items() if v > 0}

# set
{i for i in nums}

# generator (惰性求值)
(i for i in range(10**9))      # 不占内存
```

---

## 四、字符串

```python
s = "hello world"
s.split()              # ['hello', 'world']
s.split(',')
' '.join(['a', 'b'])   # 'a b'
s.strip()              # 去首尾空白
s.lower() / s.upper()
s.startswith('he')
s.endswith('ld')
s.replace('old', 'new')
s.find('lo')           # 返回索引，找不到返回 -1
s.count('l')           # 出现次数
s.isdigit() / s.isalpha()

# 格式化
f"x={x}, y={y}"
"{} {}".format(x, y)
```

---

## 五、内置函数

| 函数 | 用途 | 示例 |
|------|------|------|
| `enumerate(seq)` | 带索引遍历 | `for i, v in enumerate(lst)` |
| `zip(a, b)` | 并行遍历 | `for x, y in zip(a, b)` |
| `map(fn, seq)` | 映射 | `list(map(str, nums))` |
| `filter(fn, seq)` | 过滤 | `list(filter(lambda x: x>0, nums))` |
| `any(seq)` / `all(seq)` | 任一为真 / 全部为真 |
| `sum(seq)` / `max` / `min` | 聚合 |
| `len(seq)` | 长度 |
| `reversed(seq)` | 反向迭代器 |
| `isinstance(x, int)` | 类型检查 |
| `chr(65)` → `'A'` | 码点→字符 |
| `ord('A')` → `65` | 字符→码点 |
| `divmod(10, 3)` → `(3, 1)` | 商和余数 |
| `pow(x, y, mod)` | 幂取模 `x**y % mod` |

---

## 六、常用标准库

### 6.1 collections

```python
from collections import defaultdict, Counter, deque, OrderedDict

# defaultdict — 访问不存在的 key 自动创建默认值
d = defaultdict(int)      # 默认 0
d = defaultdict(list)     # 默认 []
d = defaultdict(set)      # 默认 set()
d['a'] += 1               # 无需判断 key 是否存在

# Counter — 频次统计
c = Counter('abracadabra')
c.most_common(2)          # [('a', 5), ('b', 2)]
c['a']                    # 5

# deque — 双端队列 (两端 O(1))
dq = deque([1, 2, 3])
dq.append(4)              # 右侧追加
dq.appendleft(0)          # 左侧追加
dq.pop()                  # 右侧弹出
dq.popleft()              # 左侧弹出（O(1)，优于 list.pop(0) 的 O(n)）

# OrderedDict — 有序字典 (Python 3.7+ dict 已默认有序)
od = OrderedDict()
od.move_to_end(key)       # 移到末尾 (LRU 缓存常用)
od.popitem(last=False)    # 弹出首元素 (FIFO)
od.popitem(last=True)     # 弹出末元素 (LIFO)
```

### 6.2 heapq — 堆 / 优先队列

```python
import heapq

heap = []
heapq.heappush(heap, item)
heapq.heappop(heap)       # 弹出最小值（小顶堆）
heapq.heapify(lst)        # 原地建堆 O(n)

# 大顶堆 (Python 只有小顶堆)
heapq.heappush(heap, -x)
-x = heapq.heappop(heap)

# 自定义排序 — 用 tuple
heapq.heappush(heap, (priority, item))

# 获取前 k 大
heapq.nlargest(k, nums)
heapq.nsmallest(k, nums)
```

### 6.3 bisect — 二分查找

```python
import bisect

# 在有序数组中查找插入位置
bisect.bisect_left(arr, x)   # 左侧插入位置（第一个 ≥ x）
bisect.bisect_right(arr, x)  # 右侧插入位置（第一个 > x）

# 直接插入
bisect.insort(arr, x)        # O(n) 因为要移动元素
```

### 6.4 itertools

```python
from itertools import permutations, combinations, product, accumulate

# 排列 / 组合
permutations([1, 2, 3], 2)   # 排列 P(3,2)
combinations([1, 2, 3], 2)   # 组合 C(3,2)
product([1, 2], ['a', 'b'])  # 笛卡尔积
accumulate([1, 2, 3])        # 前缀和 [1,3,6]

# 无限迭代器
count(10, 2)                 # 10, 12, 14, ...
cycle('ABC')                 # A,B,C,A,B,C,...
repeat('x', 3)               # x,x,x
```

### 6.5 functools

```python
from functools import lru_cache, reduce, cmp_to_key

# lru_cache — 记忆化递归 / DP
@lru_cache(None)             # None = 无上限
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# reduce — 累积归约
from operator import add, mul
reduce(add, [1, 2, 3])       # 6
reduce(mul, [1, 2, 3, 4])    # 24

# cmp_to_key — 旧式 cmp 转 key
sorted(lst, key=cmp_to_key(lambda a, b: a - b))
```

### 6.6 random

```python
import random

random.randint(0, 10)        # [0, 10] 闭区间
random.random()              # [0, 1) 浮点数
random.choice(lst)           # 随机选一个
random.shuffle(lst)          # 原地打乱
random.sample(lst, k)        # 不放回抽样 k 个
```

### 6.7 math

```python
import math

math.gcd(a, b)               # 最大公约数
math.lcm(a, b)               # 最小公倍数 (3.9+)
math.isqrt(n)                # 整数平方根
math.comb(n, k)              # 组合数 C(n,k) (3.8+)
math.perm(n, k)              # 排列数 P(n,k) (3.8+)
math.inf                     # 无穷大
math.ceil(3.2) / math.floor(3.9)
abs(x)                       # 内置绝对值
```

---

## 七、dataclass

### 7.1 基础用法

```python
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Point:
    x: int
    y: int
    label: str = "origin"          # 有默认值的放后面

p = Point(3, 4)
print(p)                           # Point(x=3, y=4, label='origin')
p2 = Point(3, 4)
p == p2                            # True（值相等，非 id 相等）
```

### 7.2 `field()` 高级用法

```python
@dataclass
class TrieNode:
    children: dict[str, 'TrieNode'] = field(default_factory=dict)  # 可变默认值
    is_end: bool = False
    count: int = field(default=0, repr=False)  # 不在 __repr__ 中显示
    size: int = field(default=0, compare=False) # 不参与相等比较
```

### 7.3 常用参数

| 参数 | 含义 |
|------|------|
| `init=True` | 生成 `__init__` |
| `repr=True` | 生成 `__repr__` |
| `eq=True` | 生成 `__eq__`（值比较） |
| `order=False` | 生成 `__lt__` `__le__` `__gt__` `__ge__` |
| `frozen=False` | 设为不可变（实例化后不能改属性） |
| `slots=True` | 使用 `__slots__` 节省内存 (3.10+) |

```python
@dataclass(frozen=True)      # 不可变，可做 dict 的 key
class FrozenPoint:
    x: int
    y: int
```

### 7.4 `__post_init__`

```python
@dataclass
class Rectangle:
    width: int
    height: int
    area: int = field(init=False)   # 不在 __init__ 参数中

    def __post_init__(self):
        self.area = self.width * self.height
```

---

## 八、类型提示 (typing)

```python
from typing import List, Dict, Tuple, Set, Optional, Union, Any

# 基础
nums: List[int] = []
d: Dict[str, int] = {}
t: Tuple[int, str] = (1, "a")
s: Set[int] = {1, 2, 3}

# Optional = 可以为 None
def f(x: Optional[int] = None) -> int:
    pass

# Union = 多选一
def g(x: Union[int, str]) -> str:
    pass

# Any = 任意类型
def h(x: Any) -> Any:
    pass

# Callable = 函数类型
from typing import Callable
def apply(fn: Callable[[int, int], int], a: int, b: int) -> int:
    return fn(a, b)

# 递归引用（需要 from __future__ import annotations）
from __future__ import annotations

@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = None    # Python 3.10+ 用 | 代替 Optional
    right: TreeNode | None = None
```

---

## 九、文件 I/O

```python
with open('file.txt', 'r') as f:
    content = f.read()           # 全读
    lines = f.readlines()        # 按行读

with open('file.txt', 'w') as f:
    f.write('hello\n')

# 逐行读（大文件）
with open('file.txt') as f:
    for line in f:
        process(line)

# 模式: 'r' 读, 'w' 写(覆盖), 'a' 追加, 'rb'/'wb' 二进制
```

---

## 十、实用技巧

```python
# 海象运算符 :=  (Python 3.8+)
if (n := len(lst)) > 10:
    print(f"太长: {n}")

# while 中读写
while (line := f.readline()):
    process(line)

# match-case (Python 3.10+)
match value:
    case 0:
        print("zero")
    case [a, b]:                   # 解构 list
        print(a, b)
    case {"key": v}:               # 解构 dict
        print(v)
    case _:
        print("other")

# 整除 / 取模
5 // 2    # 2
5 % 2     # 1
# 注意：Python 取模结果符号与除数一致
-5 % 3    # 1

# 位运算
a & b     # AND
a | b     # OR
a ^ b     # XOR
~a        # NOT
a << 1    # 左移 (×2)
a >> 1    # 右移 (÷2)

# 快速交换
a, b = b, a

# 常用逻辑
if not nums:        # 空列表为 False
if not s:           # 空字符串为 False
if d:               # 非空字典为 True

# 遍历方向数组
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for dx, dy in directions:
    nx, ny = x + dx, y + dy
```
