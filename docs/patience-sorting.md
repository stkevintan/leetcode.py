# 耐心排序 (Patience Sorting) — LIS 的 O(n log n) 解法

---

## 一、问题

给定数组 `nums`，求**最长严格递增子序列**的长度 (LIS)。

```
输入: [10, 9, 2, 5, 3, 7, 101, 18]
输出: 4
解释: 最长递增子序列是 [2, 3, 7, 101] 或 [2, 5, 7, 101]
```

---

## 二、tails 数组

**定义**：`tails[i]` = 长度为 `i+1` 的递增子序列的**最小可能结尾值**。

核心操作：遍历每个元素，**替换 tails 中第一个 ≥ 它的值**（找不到就追加）。

### 模拟

```
nums = [10, 9, 2, 5, 3, 7, 101, 18]

x=10:  tails = [10]                 长度为 1 的最优尾 = 10
x=9:   tails = [9]                  9 替换 10（降低门槛）
x=2:   tails = [2]                  同样
x=5:   tails = [2, 5]               5 > 2，扩展长度
x=3:   tails = [2, 3]               3 替换 5（长度 2 的门槛从 5 降到 3）
x=7:   tails = [2, 3, 7]            扩展
x=101: tails = [2, 3, 7, 101]       扩展
x=18:  tails = [2, 3, 7, 18]        18 替换 101

答案: len(tails) = 4
```

---

## 三、代码

```python
import bisect

def lengthOfLIS(nums):
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)   # 第一个 ≥ x 的位置
        if i == len(tails):
            tails.append(x)                 # x 比所有都大 → 扩展
        else:
            tails[i] = x                    # 替换 → 降低该长度的门槛
    return len(tails)
```

---

## 四、为什么 tails 是递增的

**数学归纳**：

1. 初始：`tails=[]`，空数组是递增的
2. 新元素 `x` 到来，找到第一个 `tails[i] ≥ x`
   - 若 `i > 0`，则 `tails[i-1] < x`（因为 `i` 是第一个≥x的）
   - 替换后：`tails[i-1] < x = tails[i] < tails[i+1]`（因为 `tails[i+1] ≥ 旧 tails[i] > x` 不成立，实际上要分情况）
3. 更直观：每个长度的"最优尾"只会越来越小，不会影响单调性

可以严格证明：`tails` 始终保持严格递增。

---

## 五、为什么 tails 只保证长度对

`tails` 存的**不是真实的子序列**，只是"门槛记录"。

```
nums = [3, 4, 5, 1, 2]
        0  1  2  3  4

x=3: tails = [3]
x=4: tails = [3, 4]
x=5: tails = [3, 4, 5]
x=1: tails = [1, 4, 5]      ← 1 替换 3
x=2: tails = [1, 2, 5]      ← 2 替换 4

最终 tails = [1, 2, 5]，长度 = 3  ✓
但 [1,2,5] 在原数组中不是递增序列:
  1 在索引 3, 2 在索引 4, 5 在索引 2
  → 5(索引2) 在 1(索引3) 前面，不可能同时取到 ❌

真正的 LIS: [3, 4, 5]
```

**替换操作只看值的大小（降低门槛），不关心位置先后。**

---

## 六、如果要还原真实 LIS

需要额外记录每个元素"接在谁后面"：

```python
def lengthOfLIS_with_path(nums):
    tails = []
    prev = [-1] * len(nums)      # prev[i] = 第 i 个元素的前驱索引
    indices = []                  # indices[k] = 长度为 k 的尾元素在原数组的索引

    for i, x in enumerate(nums):
        p = bisect.bisect_left(tails, x)
        if p == len(tails):
            tails.append(x)
            indices.append(i)
        else:
            tails[p] = x
            indices[p] = i
        if p > 0:
            prev[i] = indices[p - 1]   # 接在前一个长度的尾元素后面

    # 回溯还原
    path = []
    idx = indices[-1]
    while idx != -1:
        path.append(nums[idx])
        idx = prev[idx]
    path.reverse()
    return len(tails), path
```

---

## 七、为什么叫"耐心排序" (Patience Sorting)

这个算法等价于**纸牌游戏**：

```
规则:
  1. 从左到右发牌
  2. 每张牌放在最左边那堆"牌顶 ≥ 这张牌"的堆上
  3. 如果所有牌堆的牌顶都 < 这张牌，开新堆

牌堆数 = LIS 长度

[10, 9, 2, 5, 3, 7, 101, 18]

堆1: 10        ←
堆1: 9         ← 9 替换 10
堆1: 2         ←
堆1: 2  堆2: 5 ← 5 无法放堆 1(2<5)，开新堆
堆1: 2  堆2: 3 ← 3 替换 5
堆1: 2  堆2: 3  堆3: 7  ←
堆1: 2  堆2: 3  堆3: 7  堆4: 101 ←
堆1: 2  堆2: 3  堆3: 7  堆4: 18  ←

堆数 = 4 = LIS 长度
```

---

## 八、适用场景

任何"维护不同长度的最优状态"的问题都可以套这个模板：

| 问题 | tails 含义 | 操作 |
|------|-----------|------|
| LIS (300) | 各长度的最小尾值 | `bisect_left` + 替换/追加 |
| 最长非递减子序列 | 各长度的最小尾值 | `bisect_right`（允许等号） |
| 俄罗斯套娃信封 (354) | 先排序一维，再 LIS | 同上 |
| 最少递增子序列数 | 反向思考 | Dilworth 定理 |
| 最少箭射气球 (452) | 维护"各组的最小尾值" | 类似多重 patience sorting |

---

## 九、核心记忆

```
tails[i] = 长度为 i+1 的最优结尾门槛
永远递增 → 可在其上二分

遇到新元素 x:
  找到第一个 ≥ x 的 tails[i]
  替换它 → "这个长度的门槛现在更低了"
  
  找不到？append → "出现了一个比所有门槛都大的值，长度+1"
```

> **tails 的长度永远是答案，但 tails 的内容不一定是合法的子序列。**
