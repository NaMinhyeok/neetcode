# 200. Number of Islands

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Graphs |
| NeetCode | [문제 링크](https://neetcode.io/problems/number-of-islands) |
| LeetCode | [문제 링크](https://leetcode.com/problems/number-of-islands/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=pV2kpPD66nE) |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |

---

## 문제 설명

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

---


