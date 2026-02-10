# 329. Longest Increasing Path In a Matrix

| 항목 | 내용 |
|------|------|
| 난이도 | Hard |
| 카테고리 | 2-D Dynamic Programming |
| NeetCode | [문제 링크](https://neetcode.io/problems/longest-increasing-path-in-a-matrix) |
| LeetCode | [문제 링크](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=wCc_nd-GiEc) |
| Topics | Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix |

---

## 문제 설명

Given an `m x n` integers `matrix`, return *the length of the longest increasing path in* `matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You **may not** move **diagonally** or move **outside the boundary** (i.e., wrap-around is not allowed).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg)

```
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg)

```
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```

**Example 3:**

```
Input: matrix = [[1]]
Output: 1
```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 231 - 1`

---


