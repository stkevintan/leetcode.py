# Boyer-Moore 投票算法 — 多数元素 O(n) / O(1)

---

## 一、问题

找出数组中出现次数 **超过 ⌊n/2⌋** 的元素（保证存在）。

---

## 二、算法：一场内战

```
核心操作:
  count == 0 → 换候选人
  num == candidate → count += 1  (增援)
  num != candidate → count -= 1  (同归于尽)
```

### 模拟

```
nums = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7]

7 → candidate=7, count=1        "7 上场"
7 → count=2                     "7 增援"
5 → count=1                     "7 与 5 同归于尽一个"
7 → count=2
5 → count=1
1 → count=0                     "全部同归于尽！"
5 → candidate=5, count=1        "新候选人 5 上场"
7 → count=0                     "又同归于尽"
5 → candidate=5, count=1
5 → count=2
7 → count=1
7 → count=0

# 数组遍历完了，但根据定义多数元素 > n/2，最后 offset 为正的就是它
# 实际上 LeetCode 169 保证存在多数元素，return candidate 即答案
```

### 代码

```python
def majorityElement(nums: List[int]) -> int:
    candidate = nums[0]
    count = 1
    for num in nums[1:]:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
```

---

## 三、为什么正确

将数组分成两个阵营：**多数派 M** 和 **少数派 (其余所有人)**。

```
多数元素出现次数 > n/2
其余所有元素总次数 < n/2

每次 count -= 1:
  消耗一个 M 和一个非 M

最坏情况：所有非 M 都用来抵消 M
  M 剩余 = count(M) - count(非M) > n/2 - n/2 = 0
  → M 永远至少剩 1 票
```

**`count` 归零时**：说明目前为止的混战中，M 和非 M 同归于尽了。剩下的子数组中 M 占比更高，问题不变，重新来。

---

## 四、变体：推广到 ⌊n/3⌋

要找出现次数超过 n/3 的所有元素（最多两个）。

```python
def majorityElement(nums: List[int]) -> List[int]:
    cand1 = cand2 = None
    cnt1 = cnt2 = 0

    for num in nums:
        if num == cand1:
            cnt1 += 1
        elif num == cand2:
            cnt2 += 1
        elif cnt1 == 0:
            cand1, cnt1 = num, 1
        elif cnt2 == 0:
            cand2, cnt2 = num, 1
        else:
            cnt1 -= 1              # 三败俱伤：num, cand1, cand2 各减一
            cnt2 -= 1

    # 验证
    return [x for x in (cand1, cand2)
            if x is not None and nums.count(x) > len(nums) // 3]
```

核心推广：**k 个候选人时，新元素如果和所有候选人都不等，所有人票数各减 1（k 败俱伤）**。

---

## 五、对比

| 方法 | 时间 | 空间 |
|------|:---:|:---:|
| 排序取中位数 | O(n log n) | O(1) |
| HashMap 计数 | O(n) | O(n) |
| **Boyer-Moore** | **O(n)** | **O(1)** |
| 随机采样 | O(∞) 期望 | O(1) |
| 分治 | O(n log n) | O(log n) |

Boyer-Moore 是唯一的同时 O(n) 且 O(1) 的解。

---

## 六、局限性

Boyer-Moore **只适用于"保证存在"的场景**。如果需要返回不存在时的 -1，必须验证：

```python
def majorityElement(nums):
    cand, cnt = nums[0], 1
    for num in nums[1:]:
        if cnt == 0:
            cand = num
        cnt += 1 if num == cand else -1
    # 验证
    return cand if nums.count(cand) > len(nums) // 2 else -1
```
