# 19. Remove Nth Node From End of List

| 항목 | 내용 |
|------|------|
| 난이도 | Medium |
| 카테고리 | Linked List |
| NeetCode | [문제 링크](https://neetcode.io/problems/remove-nth-node-from-end-of-list) |
| LeetCode | [문제 링크](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) |
| 영상 풀이 | [NeetCode YouTube](https://www.youtube.com/watch?v=XVuQxVej6y8) |
| Topics | Linked List, Two Pointers |

---

## 문제 설명

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2:**

```
Input: head = [1], n = 1
Output: []
```

**Example 3:**

```
Input: head = [1,2], n = 1
Output: [1]
```

**Constraints:**

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

**Follow up:** Could you do this in one pass?

---



<details><summary>💡 Hint 1</summary>

Maintain two pointers and update one with a delay of n steps.

</details>



