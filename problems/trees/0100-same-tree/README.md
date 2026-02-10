# 100. Same Tree

| 항목 | 내용 |
|------|------|
| 난이도 | Easy |
| 카테고리 | Trees |
| NeetCode | [문제 링크](https://neetcode.io/problems/same-tree) |
| LeetCode | [문제 링크](https://leetcode.com/problems/same-tree/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=vRbbcKXCxOw) |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |

---

## 문제 설명

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```
Input: p = [1,2], q = [1,null,2]
Output: false
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

**Constraints:**

- The number of nodes in both trees is in the range `[0, 100]`.
- `-104 <= Node.val <= 104`

---


