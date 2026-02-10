# 25. Reverse Nodes In K Group

| 항목 | 내용 |
|------|------|
| 난이도 | Hard |
| 카테고리 | Linked List |
| NeetCode | [문제 링크](https://neetcode.io/problems/reverse-nodes-in-k-group) |
| LeetCode | [문제 링크](https://leetcode.com/problems/reverse-nodes-in-k-group/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=1UOPsfP85V4) |
| Topics | Linked List, Recursion |

---

## 문제 설명

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return *the modified list*.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

**Constraints:**

- The number of nodes in the list is `n`.
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

**Follow-up:** Can you solve the problem in `O(1)` extra memory space?

---


