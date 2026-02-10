# 130. Surrounded Regions

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Graphs |
| NeetCode | [문제 링크](https://neetcode.io/problems/surrounded-regions) |
| LeetCode | [문제 링크](https://leetcode.com/problems/surrounded-regions/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=9z2BunfoZ5Y) |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |

---

## 문제 설명

You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

- **Connect**: A cell is connected to adjacent cells horizontally or vertically.
- **Region**: To form a region **connect every** `'O'` cell.
- **Surround**: A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are **completely enclosed** by `'X'` cells.

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.

**Example 1:**

**Input:** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

**Output:** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

**Explanation:**

![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

**Example 2:**

**Input:** board = [["X"]]

**Output:** [["X"]]

**Constraints:**

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.

---


