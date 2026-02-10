# 102. Binary Tree Level Order Traversal

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Trees |
| NeetCode | [문제 링크](https://neetcode.io/problems/binary-tree-level-order-traversal) |
| LeetCode | [문제 링크](https://leetcode.com/problems/binary-tree-level-order-traversal/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=6ZnyEApgFYg) |
| Topics | Tree, Breadth-First Search, Binary Tree |

---

## 문제 설명

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Example 2:**

```
Input: root = [1]
Output: [[1]]
```

**Example 3:**

```
Input: root = []
Output: []
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

---



<details><summary>💡 Hint 1</summary>

Use a queue to perform BFS.

</details>



