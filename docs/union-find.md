# 并查集：从"怎么用"到"为什么"

---

## 一、本质

并查集（Union-Find / Disjoint Set Union）维护一堆**不相交的集合**，只回答两个问题：

1. **查**（find）：`x` 属于哪个集合？
2. **并**（union）：把 `x`、`y` 所在的两个集合合并成一个。

形象模型：**帮派老大**。每个元素认一个 `parent`，一路向上找，最顶上的"老大"（`parent[x] == x`）就是集合代表。两个元素同集合 ⟺ 老大相同。

```
      0        3
     / \        \
    1   2        4
   ↑ 集合 A    ↑ 集合 B
   find(2) = 0   find(4) = 3
```

---

## 二、核心操作

### find：找根 + 路径压缩

```python
def find(x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent[x])   # 路径压缩：一步挂到根上
    return parent[x]
```

**路径压缩**：查找过程中把沿途每个节点直接挂到根，下次查找就是 O(1)。

```
查找前:  0 → 1 → 2 → 3        (0 是根)
查找后:  0 ← 1 ← 2 ← 3        (全部直接指向 0)
```

### union：合并两个集合

```python
def union(a: int, b: int) -> None:
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[ra] = rb          # 一个根挂到另一个根下
```

注意：合并的是**根**，不是节点本身——忘记 `find` 直接改 `parent[a] = b` 是最常见的错误。

---

## 三、按秩合并：防止退化成链

只做路径压缩，最坏仍可能退化成链。合并时让**矮树挂到高树**下：

```python
rank = [0] * n

def union(a: int, b: int) -> None:
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[ra] = rb
        rank[rb] += 1
```

```
矮挂高:        高挂矮:
  0   +  3        0  +  3
 / \     |       /    / \
1   2    4      1    3   4
                |    ↑ 高度 +1
                2    (错误方向)
```

- `rank` 只在两树等高时才 `+1`；
- `rank[x]` 只在 `x` 是根时才有意义。

---

## 四、复杂度

同时使用**路径压缩 + 按秩合并**，单次操作均摊为**反阿克曼函数** $\alpha(n)$，实践中 $\alpha(n) \le 4$，可视为近似 $O(1)$。

| 配置 | 均摊复杂度 |
|------|-----------|
| 裸 find（无优化） | $O(n)$ 最坏 |
| 只路径压缩 | $O(\log n)$ 均摊 |
| 路径压缩 + 按秩 | $O(\alpha(n)) \approx O(1)$ |

---

## 五、标准模板（Python）

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n      # 可选：集合大小，用于需要时
        self.count = n           # 可选：连通分量个数

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False          # 已在同一集合，合并失败
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True
```

`union` 返回 `False` 意味着"这两个点原本就连通"——这个信号在判环类题目里非常关键。

---

## 六、典型题型

| 题号 | 题目 | 要点 |
|------|------|------|
| 547 | 省份数量 | 统计连通分量个数（也可 DFS/BFS） |
| 200 | 岛屿数量 | 二维网格转一维编号 |
| 684 | 冗余连接 | 遍历边，`union` 返回 `False` 的就是多余的边 |
| 685 | 冗余连接 II | 有向图，分"入度为 2"和"有环"两种情况讨论 |
| 990 | 等式方程的可满足性 | 先合并所有 `==`，再检查 `!=` |
| 399 | 除法求值 | **带权并查集**，边权 = 两数比值 |
| 128 | 最长连续序列 | 也可用哈希 $O(n)$，并查集是另一种思路 |
| 721 | 账户合并 | 邮箱为节点，按人合并 |
| 1319 | 连通网络的操作次数 | 边数不足则 -1，否则 `连通块数 - 1` |
| 1202 | 交换字符串中的元素 | 同一集合内字符排序再填回 |
| 947 | 移除最多的同行或同列石头 | 行列作为两类节点合并 |

### 判环模板（684 类）

```python
for u, v in edges:
    if not uf.union(u, v):
        return [u, v]     # 此边出现前两端已连通 → 成环
```

---

## 七、进阶变体

### 带权并查集

边带权重，`find` 时路径压缩需要**累加权值**，`union` 时按关系设定根之间的权。

```
x → y 的边权 w 表示 v[x] / v[y] = w（399 除法求值）
压缩时: weight[x] 变成 x 到根的累积权
```

```python
def find(x):
    if parent[x] != x:
        root = find(parent[x])
        weight[x] *= weight[parent[x]]   # 先压缩父亲，再累积
        parent[x] = root
    return parent[x]
```

### 反集 / 敌人集

处理"必须分开"的关系：开 $2n$ 个点，`x` 与 `x+n` 互为敌人。如 [990] 的推广版、"食物链"问题。

### 可撤销并查集

用**按大小合并且不做路径压缩**，合并时记录操作日志，按栈序撤销——用于需要回溯的场景（如可撤销 Kruskal）。

---

## 八、常见错误清单

| 错误 | 后果 |
|------|------|
| `union` 里写 `parent[a] = b` 而不是 `parent[find(a)] = find(b)` | 集合没真正合并 |
| 忘记路径压缩（直接 `while parent[x] != x: x = parent[x]` 且不更新） | 退化 $O(n)$ |
| 统计根时用 `parent[i] == i` 但没对每个 `i` 调 `find` | 中间节点漏统计 |
| `rank` 在非根节点上比较 | 数据无意义 |
| 二维网格忘了 `r * cols + c` 编码 | 下标越界 / 错误合并 |
| 用 `parent` 直接判断连通（`parent[a] == parent[b]`） | 只对根成立，普通节点必错 |

---

## 九、685 冗余连接 II：有向图的两个陷阱

### 问题

$n$ 个点 $n$ 条有向边，删掉**一条**边后变成以某个点为根的树。找出这条多余的边。

### 为什么不能直接套 684

无向版 684：`union` 失败的第一条边就是答案。有向版**不成立**：

```
edges = [[2,1],[3,1],[4,2],[1,4]]
union 到 [1,4] 时 find(1) == find(4) → 返回 [1,4] ❌
正确答案是 [2,1]（节点 1 入度为 2，删的是指向它的边）
```

### 两分法

| 情况 | 特征 | 答案 |
|------|------|------|
| 一 | 存在入度为 2 的节点 v | 指向 v 的两条边之一：先试删后出现的，不行就删另一条 |
| 二 | 无入度为 2 | 图中恰有一个环，第一条 `union` 失败的边即答案 |

**为什么情况二一定只有一个环**：无入度 2 时每个点入度恰为 1（总入度 $n$ 分给 $n$ 个点且都不超过 1）。若有两个独立环，删一条边还剩一个环，与题意矛盾。

**为什么情况二第一条成环边就是答案**：唯一的环正是冗余边闭合的；按顺序合并，第一个让两端已连通的边就是闭合该环的那条边。

### 判树技巧

情况一试删某条边后，剩 $n-1$ 条边：**无环 ⟺ 是树**（$n$ 点 $n-1$ 边无环必连通），所以并查集只需检查所有 `union` 都成功，无需单独验证可达性。

### 代码

```python
class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)

        def find(parent: list[int], x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # 路径减半
                x = parent[x]
            return x

        def is_tree(skip: int) -> bool:
            parent = list(range(n + 1))
            for i, (u, v) in enumerate(edges):
                if i == skip:
                    continue
                ru, rv = find(parent, u), find(parent, v)
                if ru == rv:
                    return False
                parent[ru] = rv
            return True

        indeg = [0] * (n + 1)
        for u, v in edges:
            indeg[v] += 1
        cand = [i for i, (u, v) in enumerate(edges) if indeg[v] == 2]
        if cand:
            i2, i1 = cand[1], cand[0]
            return edges[i2] if is_tree(i2) else edges[i1]

        parent = list(range(n + 1))
        for u, v in edges:
            ru, rv = find(parent, u), find(parent, v)
            if ru == rv:
                return [u, v]
            parent[ru] = rv
```

复杂度 $O(n\,\alpha(n))$，比逐边删除暴力验证的 $O(n^2)$ 快一个数量级。

---

## 十、一句话总结

并查集 = **集合的合并与归属查询**；路径压缩 + 按秩合并让它近似 $O(1)$；`union` 的返回值本身就是"是否成环"的判据，而连通分量数 = 根的个数。
