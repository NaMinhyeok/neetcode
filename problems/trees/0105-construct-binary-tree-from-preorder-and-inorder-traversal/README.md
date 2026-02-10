# 105. Construct Binary Tree From Preorder And Inorder Traversal

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Trees |
| NeetCode | [문제 링크](https://neetcode.io/problems/construct-binary-tree-from-preorder-and-inorder-traversal) |
| LeetCode | [문제 링크](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=ihj4IQGZ2zc) |
| Topics | Array, Hash Table, Divide and Conquer, Tree, Binary Tree |

---

## 문제 설명

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return *the binary tree*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2:**

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

**Constraints:**

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of **unique** values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is **guaranteed** to be the preorder traversal of the tree.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.

---


