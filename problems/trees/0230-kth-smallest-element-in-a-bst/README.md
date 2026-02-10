# 230. Kth Smallest Element In a Bst

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Trees |
| NeetCode | [문제 링크](https://neetcode.io/problems/kth-smallest-element-in-a-bst) |
| LeetCode | [문제 링크](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=5LUXSvjmGCw) |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |

---

## 문제 설명

Given the `root` of a binary search tree, and an integer `k`, return *the* `kth` *smallest value (**1-indexed**) of all the values of the nodes in the tree*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

**Constraints:**

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 104`
- `0 <= Node.val <= 104`

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

---



<details><summary>💡 Hint 1</summary>

Try to utilize the property of a BST.

</details>


<details><summary>💡 Hint 2</summary>

Try in-order traversal. (Credits to @chan13)

</details>


<details><summary>💡 Hint 3</summary>

What if you could modify the BST node's structure?

</details>


<details><summary>💡 Hint 4</summary>

The optimal runtime complexity is O(height of BST).

</details>



