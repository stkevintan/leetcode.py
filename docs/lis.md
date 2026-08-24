# LIS 最长递增子序列：从 O(n²) 到 O(n log n)

---

## 一、问题定义

给定数组 `nums`，求**最长严格递增子序列**（Longest Increasing Subsequence）的长度。

```
输入: [10, 9, 2, 5, 3, 7, 101, 18]
输出: 4          # [2, 3, 7, 101] 或 [2, 5, 7, 101]
```

先厘清两个容易混淆的概念：

| 概念 | 定义 | 例：`[3,1,4,2]` |
|------|------|------|
| 子数组/子串 | 必须连续 | `[3,1]`、`[1,4]` 是；`[3,4]` 不是 |
| 子序列 | 保持相对顺序，可不连续 | `[3,4]`、`[1,2]` 都是 |
| 严格递增 | 后一个 > 前一个 | `[1,1]` 不算 |
| 非降 | 后一个 ≥ 前一个 | `[1,1]` 算 |

LIS 问的是**子序列 + 严格递增**（除非题目明说非降）。

---

## 二、DP 解法：O(n²)

### 定义

`dp[i]` = **以 `nums[i]` 结尾**的最长递增子序列长度。

> 为什么是"以 i 结尾"？因为子序列的合法性取决于最后一个元素，必须固定结尾才能比较大小并转移。

### 转移

```python
dp[i] = 1 + max(dp[j])   for j < i 且 nums[j] < nums[i]
```

若不存在这样的 `j`，则 `dp[i] = 1`。

```
nums = [10, 9, 2, 5, 3, 7, 101, 18]
dp   = [ 1, 1, 1, 2, 2, 3,   4,  4]

例如 dp[5] (nums=7): 前面比 7 小的有 2(1), 5(2), 3(2)
       → dp[5] = max(1,2,2) + 1 = 3
```

### 代码

```python
def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)          # 不是 dp[-1]！最长序列不一定以最后元素结尾
```

**坑**：答案是 `max(dp)` 而非 `dp[-1]`；`dp` 初始化为 1（每个元素自身构成长度 1）。

---

## 三、贪心 + 二分：O(n log n)

DP 的瓶颈在于找 `max(dp[j])`。换一个状态定义，把"找"变成"二分"。

### tails 定义

`tails[i]` = 长度为 `i+1` 的递增子序列的**最小可能结尾值**。

遍历每个 `x`，在 `tails` 中找**第一个 `≥ x` 的位置 `i`**：

- 找不到（`x` 比所有结尾都大）→ `append(x)`，长度 +1；
- 找到 → `tails[i] = x`，把该长度的"门槛"压低。

```
nums = [10, 9, 2, 5, 3, 7, 101, 18]

x=10:  [10]
x=9:   [9]                 9 替换 10
x=2:   [2]
x=5:   [2, 5]              扩展
x=3:   [2, 3]              3 替换 5（门槛 5→3）
x=7:   [2, 3, 7]           扩展
x=101: [2, 3, 7, 101]      扩展
x=18:  [2, 3, 7, 18]       18 替换 101

答案: len(tails) = 4
```

### 代码

```python
import bisect

def lengthOfLIS(nums: List[int]) -> int:
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)   # 第一个 ≥ x
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```

复杂度 $O(n \log n)$，空间 $O(n)$。详细证明见 [patience-sorting.md](patience-sorting.md)。

### 严格 vs 非降：bisect_left 与 bisect_right

| 目标 | 用哪个 | 逻辑 |
|------|--------|------|
| 严格递增 | `bisect_left` | 找到 `≥ x` 替换，等值不能共存 → 长度不会因重复元素增长 |
| 非降 | `bisect_right` | 找到 `> x` 替换，等值可以接在后面 → 重复元素可增长 |

```
nums = [1, 1, 1]
严格: bisect_left → tails 始终 [1]，答案 1
非降: bisect_right → tails = [1,1,1]，答案 3
```

### 手写二分版（无 bisect）

```python
def lengthOfLIS(nums: List[int]) -> int:
    tails = []
    for x in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < x:      # 严格: < ；非降: <=
                lo = mid + 1
            else:
                hi = mid
        if lo == len(tails):
            tails.append(x)
        else:
            tails[lo] = x
    return len(tails)
```

---

## 四、重要性质与误区

1. **`tails` 不是真实子序列**。它只记录"门槛"，其中的元素在原数组中可能顺序错乱：

```
nums = [3, 4, 5, 1, 2]
tails 演化: [3] → [3,4] → [3,4,5] → [1,4,5] → [1,2,5]
[1,2,5] 不是合法子序列（1 在 5 之后），但长度 3 是对的。
```

2. **`tails` 始终严格递增**——这是二分可行的前提，可用归纳证明。
3. **要还原具体序列**，需额外记录前驱（见 [patience-sorting.md](patience-sorting.md) 第六节）。

---

## 五、变体题

| 题号 | 题目 | 变体点 |
|------|------|--------|
| 300 | 最长递增子序列 | 原型 |
| 674 | 最长连续递增序列 | 变成**子数组**：一次遍历比较相邻即可 |
| 673 | 最长递增子序列的个数 | 记录 `count[i]`，等长时累加 |
| 354 | 俄罗斯套娃信封 | 二维：先按宽度升序、同宽按高度**降序**，再对高度求 LIS |
| 1964 | 最长有效障碍赛跑路线 | **非降**版本 → `bisect_right` |
| 1671 | 得到山形数组的最少删除次数 | 正反两次 LIS，`left[i] + right[i] - 1` 找峰 |

### 354 的关键排序

```python
envelopes.sort(key=lambda e: (e[0], -e[1]))   # 宽升序，同宽高降序
heights = [h for _, h in envelopes]
return lengthOfLIS(heights)                     # 二维问题降成一维
```

> 同宽必须按高度降序，否则同宽的信封会互相套上（宽相等不能套）。

### 673 的计数版转移

```python
dp[i] = 1; cnt[i] = 1
for j < i 且 nums[j] < nums[i]:
    if dp[j] + 1 > dp[i]:          # 找到更长的 → 重置计数
        dp[i] = dp[j] + 1
        cnt[i] = cnt[j]
    elif dp[j] + 1 == dp[i]:       # 同样长 → 累加方案
        cnt[i] += cnt[j]
ans = sum(cnt[i] for i if dp[i] == L)
```

---

## 六、解法选择

| 场景 | 解法 | 复杂度 |
|------|------|--------|
| 只求长度，n 较大 | 贪心 + 二分 | $O(n \log n)$ |
| 要还原具体序列 | 贪心 + 二分 + 前驱指针 | $O(n \log n)$ |
| 要统计个数 | DP + 计数 | $O(n^2)$ |
| 要按字典序最小等附加约束 | DP 为主 | $O(n^2)$ |

---

## 七、一句话总结

- **DP 版**：`dp[i]` 以 `i` 结尾，答案 `max(dp)`，胜在能统计个数/还原细节；
- **二分版**：`tails[i]` 是长度为 `i+1` 的最小结尾，`bisect_left`（严格）/ `bisect_right`（非降），胜在 $O(n\log n)$；
- 区分**子数组**（连续）与**子序列**（不连续），注意严格/非降的语义差异。
