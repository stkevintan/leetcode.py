# DFS / 回溯 常用技巧

---

## 一、两种 DFS 遍历模式

### 模式 A：每个元素必须处理（不可跳过）

```python
def dfs(start):
    if start == len(nums):
        return
    for choice in options[nums[start]]:
        path.append(choice)
        dfs(start + 1)          # ← 直接 +1，固定推进
        path.pop()
```

**适用**：电话号码字母组合、全排列、N 皇后（每行必须放一个）

### 模式 B：每个元素可选/可不选（可跳过）

```python
def dfs(start):
    yield path.copy()
    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(i + 1)              # ← i+1，允许跳过中间的
        path.pop()
```

**适用**：子集、组合总和（每个数可选 N 次时传 `i` 而不是 `i+1`）

---

## 二、`i` vs `i+1` — 重复选取的控制开关

```python
# 每个数最多选一次（子集、组合）
yield from dfs(i + 1, ...)

# 每个数可以选无限次（组合总和）
yield from dfs(i, ...)
```

**一句话：传 `i` 允许重复选，传 `i+1` 禁止重复选。**

---

## 三、回溯 vs 不可变传递

### 回溯（共享引用 + pop）

```python
def dfs(start):
    yield cur.copy()
    for i in range(start, len(nums)):
        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()
```

- 优点：零额外内存
- 注意：yield 时必须 `.copy()`，否则后续 pop 会污染已产出的结果

### 不可变传递（每次新建列表）

```python
def dfs(start, subset):
    yield subset
    for i in range(start, len(nums)):
        yield from dfs(i + 1, [*subset, nums[i]])
```

- 优点：无需 copy，无需 pop，代码更短
- 代价：每次递归多一次列表复制，n 不大时可忽略

---

## 四、Generator 模式 DFS

```python
from typing import Iterator

def dfs(start: int) -> Iterator[List[int]]:
    if 终止条件:
        yield cur.copy()
        return
    for i in range(start, len(nums)):
        cur.append(nums[i])
        yield from dfs(i + 1)       # 透传子递归的所有产出
        cur.pop()

# 调用方统一收集
return list(dfs(0))
```

- `yield` 产出单个结果
- `yield from` 把子递归的所有结果向上透传
- 好处：生成逻辑和收集逻辑解耦

---

## 五、Python 传参陷阱（DFS 相关）

Python 是 **传对象引用**，不是传值：

```python
def f(lst):
    lst.append(4)   # ✅ 外部可见（修改同一个对象）
    lst = [100]     # ❌ 外部不可见（仅局部变量重新绑定）

# DFS 中典型踩坑：
def dfs(cur):
    ans.append(cur)         # ❌ 存的是引用，后面 pop 会改掉它
    ans.append(cur.copy())  # ✅ 存副本，安全
```

---

## 六、常见剪枝位置

```python
def dfs(start, total):
    # 剪枝 1：超过目标直接返回（放在最前面）
    if total > target:
        return

    # 剪枝 2：等于目标记录结果
    if total == target:
        yield path.copy()
        return

    # 剪枝 3：循环内提前 break（需数组有序）
    for i in range(start, len(nums)):
        if total + nums[i] > target:
            break                    # 后面更大，全跳过
        path.append(nums[i])
        yield from dfs(i, total + nums[i])
        path.pop()
```

**剪枝的关键：数组先排序 + 提前 `break`（不是 `continue`）。**

## 七、lower bound vs upper bound
lower bound: 第一个 >= target 的元素
upper bound: 第一个 > target 的元素 
[leetcode 34](../34.在排序数组中查找元素的第一个和最后一个位置.py)

## 八、minstack
同步记录当前栈的最小值 [leetcode 155](../155.最小栈.py)