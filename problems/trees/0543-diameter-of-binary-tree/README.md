# 543. Diameter of Binary Tree

| 항목 | 내용 |
|------|------|
| 난이도 | Easy |
| 카테고리 | Trees |
| NeetCode | [문제 링크](https://neetcode.io/problems/diameter-of-binary-tree) |
| LeetCode | [문제 링크](https://leetcode.com/problems/diameter-of-binary-tree/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=bkxqA8Rfv04) |
| Topics | Tree, Depth-First Search, Binary Tree |

---

## 문제 설명

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `-100 <= Node.val <= 100`

---


