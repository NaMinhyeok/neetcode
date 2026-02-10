# 572. Subtree of Another Tree

| 항목 | 내용 |
|------|------|
| 난이도 | Easy |
| 카테고리 | Trees |
| NeetCode | [문제 링크](https://neetcode.io/problems/subtree-of-another-tree) |
| LeetCode | [문제 링크](https://leetcode.com/problems/subtree-of-another-tree/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=E36O5SWp-LE) |
| Topics | Tree, Depth-First Search, String Matching, Binary Tree, Hash Function |

---

## 문제 설명

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)

```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)

```
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

**Constraints:**

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-104 <= root.val <= 104`
- `-104 <= subRoot.val <= 104`

---



<details><summary>💡 Hint 1</summary>

Which approach is better here- recursive or iterative?

</details>


<details><summary>💡 Hint 2</summary>

If recursive approach is better, can you write recursive function with its parameters?

</details>


<details><summary>💡 Hint 3</summary>

Two trees <b>s</b> and <b>t</b> are said to be identical if their root values are same and their left and right subtrees are identical. Can you write this in form of recursive formulae?

</details>


<details><summary>💡 Hint 4</summary>

Recursive formulae can be: 
isIdentical(s,t)= s.val==t.val AND isIdentical(s.left,t.left) AND isIdentical(s.right,t.right)

</details>



