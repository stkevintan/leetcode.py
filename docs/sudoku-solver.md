# 解数独 — 回溯 + 位运算 + MRV

---

## 一、问题

给定 9×9 数独棋盘（`.` 表示空格），填满棋盘使每行、每列、每个 3×3 宫内数字 1–9 各出现一次。保证有唯一解。

---

## 二、基础解法：回溯

本质是一个**约束满足问题（CSP）**，回溯框架：

1. 选一个空格
2. 尝试所有合法数字
3. 填进去，递归；失败则撤销（恢复数字、恢复状态）
4. 找到解立即返回 `True` 层层退出

### 朴素版本（固定顺序）

```python
def dfs(pos: int) -> bool:
    if pos == len(dots):
        return True
    x, y = dots[pos]
    for v in range(1, 10):
        if 合法:
            board[x][y] = str(v)
            ...
            if dfs(pos + 1):
                return True
            board[x][y] = '.'
            ...
    return False
```

LeetCode 数据规模下已经够快，但最坏情况分支因子接近 9，搜索树可能爆炸。

---

## 三、位运算状态压缩

每个数字 v 用 `1 << v` 表示，行/列/宫各用一个整数当「位集合」：

```python
FULL = (1 << 10) - 2        # 位 1..9 全置 1

rows[i] |= mask            # 第 i 行占用情况
cols[j] |= mask
grids[i // 3][j // 3] |= mask

# 某格 (x, y) 的候选数字：
cand = FULL & ~(rows[x] | cols[y] | grids[x // 3][y // 3])
```

- 合法性判断从「遍历 9 个数字查三次」变成一次按位与
- 撤销用 `^=`（异或还原），比减法直观且幂等

---

## 四、升级一：MRV 启发式

**MRV（Minimum Remaining Values）**：每步不按固定顺序，而是挑「候选数最少」的空格先填。

- 分支因子从最多 9 降到该格实际候选数
- 候选少的格子最容易引发冲突，先解决它们能大幅剪枝
- 难棋盘上搜索树可缩小几个数量级

```python
if best is None or cand.bit_count() < best_cand.bit_count():
    best, best_cand = (i, j), cand
```

## 升级二：候选直接枚举 + 死路剪枝

- `cand == 0`：某格一个候选都没有 → 当前局面无解，**立即返回 False**（比填到后面才发现快得多）
- 枚举候选直接用 `bit = cand & -cand` 取最低位，`cand ^= bit` 消掉，不用 `for v in range(1, 10)`

---

## 五、最终代码

```python
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        n, m = len(board), len(board[0])
        FULL = (1 << 10) - 2  # 位 1..9 全置 1
        rows, cols, grids = [0] * n, [0] * m, [[0] * 3 for _ in range(3)]
        for i in range(n):
            for j in range(m):
                if board[i][j] != '.':
                    mask = 1 << int(board[i][j])
                    rows[i] |= mask
                    cols[j] |= mask
                    grids[i // 3][j // 3] |= mask

        def dfs() -> bool:
            best: tuple[int, int] | None = None
            best_cand = 0
            for i in range(n):
                for j in range(m):
                    if board[i][j] == '.':
                        cand = FULL & ~(rows[i] | cols[j] | grids[i // 3][j // 3])
                        if cand == 0:
                            return False
                        if best is None or cand.bit_count() < best_cand.bit_count():
                            best, best_cand = (i, j), cand
            if best is None:
                return True
            x, y = best
            cand = best_cand
            while cand:
                bit = cand & -cand
                cand ^= bit
                board[x][y] = str(bit.bit_length() - 1)
                rows[x] |= bit
                cols[y] |= bit
                grids[x // 3][y // 3] |= bit
                if dfs():
                    return True
                board[x][y] = '.'
                rows[x] ^= bit
                cols[y] ^= bit
                grids[x // 3][y // 3] ^= bit
            return False

        dfs()
```

---

## 六、常见踩坑（真实犯过的 5 个错）

1. **位编码不一致**：初始化写 `|= int(cell)`（把 5 当 0b101，标记了 1 和 4），试探时却用 `1 << v`。两处必须统一为 `1 << int(cell)`。
2. **宫索引用 `%3` 而不是 `//3`**：第 3 行和第 0 行会被算进同一个宫。
3. **回溯不恢复 board**：撤销掩码后 `board[x][y]` 还残留试过的数字，必须写回 `'.'`。
4. **没有成功信号**：找到解后不返回 `True`，调用方继续试其他值把解撤销了。回溯必须层层传 `True` 提前退出。
5. **双重循环结构**：`dfs` 里既 `for i in range(start, ...)` 又递归传 `start + 1`，每次递归都从头扫，指数级冗余。循环与递归二选一。

---

## 七、再往上：Dancing Links（DLX）

数独可转化为**精确覆盖问题**：729 行（81 格 × 9 数字）× 324 列（81 行 + 81 列 + 81 宫 + 81 格）。

Knuth 的 Algorithm X + 双向十字链表（DLX）是解数独的理论最优框架，也是当年数独求解竞赛的标准做法。思想值得了解，但面试/刷题一般不需要实现。

---

## 八、复杂度

- 理论最坏仍是指数级（数独是 NP-complete）
- MRV + 剪枝让实际搜索树远小于 $9^{81}$ 的朴素上界
- 空间：$O(81)$

---

## 九、一句话总结

**回溯框架 + 位运算压缩状态 + MRV 挑候选最少的格子 + 死路提前剪枝**，是数独求解在「代码量」与「效率」间的最佳平衡点。
