# 62. Unique Paths

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | 2-D Dynamic Programming |
| NeetCode | [문제 링크](https://neetcode.io/problems/unique-paths) |
| LeetCode | [문제 링크](https://leetcode.com/problems/unique-paths/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=IlEsdxuD4lY) |
| Topics | Math, Dynamic Programming, Combinatorics |

---

## 문제 설명

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to `2 * 109`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```
Input: m = 3, n = 7
Output: 28
```

**Example 2:**

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

**Constraints:**

- `1 <= m, n <= 100`

---


